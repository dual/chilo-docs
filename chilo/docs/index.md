# Chilo
Chilo, short for chilorhinophis (meaning two headed snake), is a lightweight, form-meets-function, opinionated (yet highly configurable) api framework.

## Features
* No route definitions needed; route based on your directory structure
* Built-in OpenAPI request and response validation
* Ease of use with gunicorn
* Generate OpenAPI spec from code base
* Infinitely customizable with middleware extensions

## Philosophy

The Chilo philosophy is to provide a dry, configurable, declarative framework, which encourages Happy Path Programming (HPP).

Happy Path Programming is an idea in which inputs are all validated before operated on. This ensures code follows the happy path without the need for mid-level, nested exceptions and all the nasty exception handling that comes with that. The library uses layers of customizable middleware options to allow a developer to easily dictate what constitutes a valid input, without nested conditionals, try/catch blocks or other coding blocks which distract from the happy path which covers the majority of the source code's intended operation.
