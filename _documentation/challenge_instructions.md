# Price Conversion (Currency & Unit) - Django HTMX Challenge Instructions for the Candidate

_Fabrizio Nastri, Dec 2024_

### Description

This repo provides the scaffolding for a simple app designed to test:

- your knowledge of:
  - Django,
  - Django templating,
  - APIs,
  - htmx
- your ability to read and understand:
  - existing code developed by someone else
  - the specifications of a given ticket / task (this current file)
- your ability to:
  - fulfill the ticket requirements / specifications
  - write clean and maintainable code
  - to follow the coding style and guidelines of the existing codebase (see `_documents/guidelines.md`)
  - to handle / debug legacy code

This tech stack is seen as a possible solution for the FlexUp MVP project, in order to minimise the work in building the front end application (this may be done at a later stage). In the FlexUp MVP, we will focus on basic functionalities with minimum effort on the UX/UI side.

The ["Tax Calculator"](https://github.com/fabrizionastri/tax_calc) app is given as an example of HTMX. Please use this as a reference for the current challenge.

### App specifications / coding exercise

- The goal of this exercise is to create a Django app that allows the user to convert prices in one currency/unit into another currency/unit
- Each conversion is stored in the database for future reference using the `Conversion` model
- The list of available system units, with their respective dimension and the their conversion rate (to the base unit of each dimension) is provided in the enums `unit.py` file
- The list of currencies is provided in the `currencies.py` file
- The converion rates must be obtained via an external API, and each time a conversion is made, the app should store it to the database using the `ExchangeRate` model.
- The app contains a single page with 2 main elements (see ["UX Mockup"](ux_mockup.pdf)):
  - a header: "Price Conversion (Currency & Unit)"
  - a form used to create, view and update a price conversion
  - a list of all conversions
    -The same form should be used to create, view and edit a conversion
- When the user submits the form:
  - the conversion should be saved in the database,
  - the list of conversions should be updated,
  - the form should be cleared.
- The list of all conversions should be on the same page, as table, under the form, and contain the following columns:
  - Nr
  - from ("153.72 €/kg")
  - to ("198.21 $/gallon")
- Prices should be rounded to 4 decimal places in the database and in the form, displayed with 2 decimals in the list
- - The user should be able to:
  - see the details of the conversion in the form by clicking on a "view/edit" button next to the conversion in the list
  - delete a conversion from the list and the database by clicking on a "delete" button next to the conversion in the list
  - create a new conversion by filling in the form and clicking on a "submit" button
  - clear the form it is filled in by clicking on a "clear" button
- Table headers for each columns should be in "Title Case"
- The page should never reload, and the user should never be redirected to another page.
  - The app should use HTMX for seamless updates.
  - when a conversion is created, updated or deleted from the list, only that signle row should be updated in the list and the header and form should remain unchanged
  - when user clicks on a "view/edit" button, the form should be updated with the conversion details, and the header and list should remain unchanged
  - when user clicks on a "delete" button, the row should be removed from the list, and the header and form should remain unchanged
- Use the default Django SQLite database
- User stories / features:
  - create a new conversion
  - list all conversions
  - view a conversion
  - edit a conversions
  - delete a conversion
- The Readme.me file should be updated with the instructions on how to install and run the app
