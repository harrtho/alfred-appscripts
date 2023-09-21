# AppScripts Alfred Workflow

[![GitHub Version][version-shield]][releases]
[![GitHub All Releases][downloads-shield]][releases]
[![GitHub][license-shield]][mit-license]

List, search and run/open AppleScripts for the active application in [Alfred][alfred].

![][preview]

## Download & Installation

Download the [latest workflow release][gh-latest-release] from GitHub. Open the workflow file to
install in Alfred.

## Usage

- `.as [<query>]` — Show/search list of AppleScripts for the active application
  - `↩` — Run the selected script.
  - `⌘ + ↩` — Open the selected script in Script Editor.
  - `⌥ + ↩` — Reveal the selected script in Finder.
- `appscripts [<query>]` — Show workflow configuration.
  - `Help` – Open this file in your browser.
  - `(No) Update Available` — Whether or not the workflow can be updated. Action the item to update
    or force an update check.
  - `Search Directories Recursively` – Whether the script directories should be searched
    recursively. Use with some caution.
  - `Edit Script Directories` — Open the configuration file in your default editor. The file
    contains a detailed description of how it works.
  - `Reset to Defaults` — Delete configuration and cache files.

## Configuration

The workflow comes with a default set of directories. These are defined in a settings file that you
can edit yourself. Use the `Edit Script Directories` option in the configuration
(keyword `appscripts`) to open the file in your editor.

These are the default directories. `{app_name}` will be replaced with the name of the currently
active application, e.g. `BBEdit` or `OmniFocus`, and `{bundle_id}` with the application's bundle
ID, e.g. `com.barebones.bbedit` or `com.omnigroup.OmniFocus2`:

- `~/Library/Scripts/Applications/{app_name}`
- `~/Library/Scripts/Applications/{bundle_id}`
- `~/Library/Application Scripts/{app_name}`
- `~/Library/Application Scripts/{bundle_id}`
- `~/Library/Application Support/{app_name}/Scripts`
- `~/Library/Application Support/{bundle_id}/Scripts`
- `~/Library/Containers/{bundle_id}/Data/Library/Application Support/{app_name}/Scripts`

Any `*.scpt`, `*.applescript`, `*.scptd` (script bundle) or `*.js` (JXA) files found within the
above directories will be shown.

If you add a directory path that doesn't contain `{app_name}` or `{bundle_id}`, it will match every
application and the scripts will always be shown. See the settings file
(`AppScript Directories.txt`) for more information.

## Bug reports and feature requests

Please use [GitHub issues][gh-issues] to report bugs or request features.

## Contributors

This Alfred Workflow comes from the [abandoned Workflow][abandoned-workflow] of
[Dean Jackson][deanishe]

## License

AppScripts Alfred Workflow is licensed under the [MIT License][mit-license]

The workflow uses the following libraries:

- [Alfred-PyWorkflow][alfred-pyworkflow] ([MIT License][mit-license])
- [docopt][docopt] ([MIT License][mit-license])

The workflow uses following icons:

- Workflow icon created by [Jono Hunt][jono]
- Other icons are from [Font Awesome][font-awesome] ([SIL OFL 1.1 license][sil-license])

[abandoned-workflow]: https://github.com/deanishe/alfred-appscripts
[alfred-pyworkflow]: https://github.com/harrtho/alfred-pyworkflow
[alfred]: https://www.alfredapp.com
[deanishe]: https://github.com/deanishe
[docopt]: https://github.com/docopt/docopt
[downloads-shield]: https://img.shields.io/github/downloads/harrtho/alfred-appscripts/total.svg
[font-awesome]: https://fontawesome.com
[gh-issues]: https://github.com/harrtho/alfred-appscripts/issues
[gh-latest-release]: https://github.com/harrtho/alfred-appscripts/releases/latest
[jono]: https://www.alfredforum.com/profile/66-jono/
[license-shield]: https://img.shields.io/github/license/harrtho/alfred-appscripts.svg
[mit-license]: https://opensource.org/licenses/MIT
[preview]: img/preview.png
[releases]: https://github.com/harrtho/alfred-appscripts/releases
[sil-license]: https://scripts.sil.org/OFL
[version-shield]: https://img.shields.io/github/release/harrtho/alfred-appscripts.svg
