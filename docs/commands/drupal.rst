Drupal Commands
===============

This section covers the specific commands available for managing Drupal projects.

Overview
--------

The `alt` tool provides a set of commands tailored for managing and administering Drupal projects. These commands help in enabling, disabling, and configuring various aspects of a Drupal project via CLI.

Enable Drupal Command
---------------------

To enable a Drupal-specific command, use the following syntax:

.. code-block:: shell

   alt command enable drupal

Example:

.. code-block:: shell

   alt command enable drupal

Output:

.. code-block:: text

   Enabled command: drupal

Disable Drupal Command
----------------------

To disable a Drupal-specific command, use the following syntax:

.. code-block:: shell

   alt command disable drupal

Example:

.. code-block:: shell

   alt command disable drupal

Output:

.. code-block:: text

   Disabled command: drupal

Available Drupal Commands
-------------------------

Below is a list of commonly used Drupal commands supported by the `alt` tool:

1. **drupal-install**: Installs Drupal.
   - **Usage**: `alt drupal install`
2. **drupal-update**: Updates Drupal to the latest version.
   - **Usage**: `alt drupal update`
3. **drupal-module-enable**: Enables a specific Drupal module.
   - **Usage**: `alt drupal module-enable <module-name>`
4. **drupal-module-disable**: Disables a specific Drupal module.
   - **Usage**: `alt drupal module-disable <module-name>`

You can get detailed information on each command using the `--help` flag.

Refer to the official Drupal documentation for more comprehensive guidelines on managing Drupal projects.

.. note::

   Ensure you have installed the necessary dependencies and have the correct permissions to run these commands.
