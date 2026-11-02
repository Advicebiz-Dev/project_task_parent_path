# Project Task Parent Path

Odoo 19 module that improves the **Convert to Task/Sub-Task** dialog.

## What it changes

In the **Parent Task** field, task suggestions are displayed as:

`Project Name / Task Name`

instead of only:

`Task Name`

This is applied only to the parent-task selector in the conversion dialog, so the normal
task name shown elsewhere in Odoo is not changed.

The autocomplete can also match the project name as well as the task name.

## Example

Before:

- Submissão do PTA por entidade
- Submissão do PTA por entidade
- Submissão do PTA por entidade

After:

- Projeto A / Submissão do PTA por entidade
- Projeto B / Submissão do PTA por entidade
- Projeto C / Submissão do PTA por entidade

## Installation

1. Copy the module folder to `custom_addons`.
2. Restart Odoo.
3. Update the Apps list.
4. Install **Project Task Parent Path**.

No database migration or configuration is required.
