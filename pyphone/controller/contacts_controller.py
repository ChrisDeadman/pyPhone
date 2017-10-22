import logging
import threading
from collections import namedtuple
from tkinter import *

import pyperclip

from pyphone import controller
from pyphone.controller import Controller
from pyphone.utils import *

Contact = namedtuple("Contact", ["display_name", "phone_numbers"])


class ContactsController(Controller):
    _log = logging.getLogger(__name__)

    _fetch_contacts_thread = None

    contacts = None

    def __init__(self, panel):
        super().__init__(panel)

        panel.bind_on_raise(self._on_raise)

        self._contact_image = load_image(self.panel, "person.png", relative_size=RelativeSize.small)
        self._number_image = load_image(self.panel, "call.png", relative_size=RelativeSize.small)

        self._contacts_tree = self.panel.contacts_tree
        self._contacts_tree.bind("<<TreeviewSelect>>", self._on_contacts_tree_select)

    def _on_raise(self):
        self._people_service = controller.GAuthController.people_service

        if self._people_service is None:
            controller.CallController.show_gauth_panel()
            return

        if self.contacts is None:
            self.contacts = []
            self._fetch_contacts_thread = threading.Thread(target=self._fetch_contacts_worker)
            self._fetch_contacts_thread.start()

    def cleanup(self):
        super().cleanup()
        if self._fetch_contacts_thread is not None:
            self._fetch_contacts_thread.join()

    def find_contact_by_number(self, phone_number):
        if self.contacts is not None:
            for contact in self.contacts:
                for contact_number in contact.phone_numbers:
                    if phone_number == contact_number:
                        return contact

        return None

    def _fetch_contacts_worker(self):
        try:
            self._fetch_contacts()
        except Exception as e:
            error_message = "{}: {}".format(type(e).__name__, e)
            self._log.exception(error_message)
            controller.CallController.show_error("Authorization failed", error_message)

    def _on_contacts_tree_select(self, event):
        selection = self._contacts_tree.selection()
        if len(selection) < 1:
            return

        item = self._contacts_tree.item(selection[0])
        item_text = item["text"]

        # expand / collapse item
        self._contacts_tree.item(selection[0], open=not item["open"])

        # copy to clipboard
        pyperclip.copy(item_text)

        # copy any phone number to dial pad
        if re.match("^[+0-9]+$", item_text):
            controller.DialController.set_phone_number(item_text)

        controller.CallController.show_dial_panel()

    def _fetch_contacts(self):
        self._log.info("Fetching google contacts...")

        results = self._people_service.people().connections().list(
            resourceName="people/me",
            pageSize=1024,
            personFields="names,phoneNumbers",
        ).execute()
        connections = results.get("connections", [])

        for person in sorted(connections, key=lambda p: _person_get_display_name(p)):
            display_name = _person_get_display_name(person)
            phone_numbers = [number["canonicalForm"] for number in person.get("phoneNumbers", [])]
            if (display_name is not None) and (len(phone_numbers) > 0):
                self.contacts.append(Contact(display_name, phone_numbers))

        for contact in self.contacts:
            contact_node = self._contacts_tree.insert("", END, text=contact.display_name, image=self._contact_image)
            numbers_node = self._contacts_tree.insert(contact_node, END, text="Numbers", open=True)
            for phone_number in contact.phone_numbers:
                self._contacts_tree.insert(numbers_node, END, text=phone_number, image=self._number_image)

        num_contacts = len(connections)
        num_contacts_with_number = len(self.contacts)
        num_contacts_without_number = num_contacts - num_contacts_with_number
        self._log.info("{} of {} contacts fetched ({} without phone number)".format(num_contacts_with_number,
                                                                                    num_contacts,
                                                                                    num_contacts_without_number))


def _person_get_display_name(person):
    names = person.get("names", [])
    return names[0]["displayName"] if len(names) > 0 else None
