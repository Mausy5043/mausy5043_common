# BUILDING

## Versionnumbers

We try to follow [semantic versioning](semver.org).
* We don't have `0` MINOR or PATCH versionnumbers. Patterns `x.0.z` and `x.y.0` do not exist.
* Testing versions are identified by odd-numbered MINOR versions
* Stable/production versions are identified by even-numbered MINOR versions
* MAJOR versions increase only when significant changes are made

## Building the package for testing

To test changes the package may be built and uploaded to [test.pypi.org](test.pypi.org)
Preferably changes are done on a separate branch.

1. Make the necessary changes...
1. In `./pyproject.toml` change the versionnumber under `[project]/version`
   * For testing we change the MINOR version to the next **odd** value
   * The first PATCH version always starts on x.y.1 and increases by +1 with every new build
   * Builds with the same versionnumber can't be uploaded to PyPi, so it's not like we have a choice
1. Run `./mkbld -b`
1. Run `./mkbld -t`  *(installation instructions are displayed on the terminal after the upload)*
1. Test the changes by installing the test package on a computer near you. *NOTE: You may have to try twice or wait a couple of minutes for the download to become available from PyPi.*
1. Rinse and repeat...
1. Execute `git commit -a; git push` to commit the changes
1. After succesfull testing create a pull request to merge the changes into the `master` branch
1. See below for updating the distribution

## Building the package for distribution

To distribute a new production version the package must be built and uploaded to [pypi.org](pypi.org)

1. Make the necessary changes...
   * Merges from a separate branch are considered MINOR changes
   * Fixes etc. may be committed directly to the `master` branch as a new PATCH version
1. In `./pyproject.toml` change the versionnumber under `[project]/version`
   * For merges we change the MINOR version to the next **even** value
   * The first PATCH version always starts on x.y.1 and increases by +1 with every new build
   * Builds with the same versionnumber can't be uploaded to PyPi, so it's not like we have a choice
1. Run `./mkbld -b`
1. Run `./mkbld -d`  *(installation instructions are displayed on the terminal after the upload)*
1. Test the changes by installing the distribution package on a computer near you. *NOTE: You may have to try twice or wait a couple of minutes for the download to become available from PyPi.*
1. Rinse and repeat...
1. Execute `git commit -a; git push` to commit the changes
1. After succesfull testing of the distribution package create a new tag on the `master` branch

## Available commands for package building
`./mkbld --build|-b` builds the distribution files
`./mkbld --dist|-d` uploads the distribution files to PyPi
`./mkbld --test|-t` uploads the dictribution files to TestPyPi
`./mkbld --discard` **discards all changes to the local copy** of the repo and pulls the current state of the repo from GitHub.
