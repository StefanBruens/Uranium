# Copyright (c) 2016 Ultimaker B.V.
# Uranium is released under the terms of the AGPLv3 or higher.

import pytest
import os.path

import UM.Settings
import UM.PluginRegistry
import UM.Settings.DefinitionContainer

from UM.Resources import Resources
from UM.MimeTypeDatabase import MimeType, MimeTypeDatabase

##  Fake container class to add to the container registry.
#
#   This allows us to test the container registry without testing the container
#   class. If something is wrong in the container class it won't influence this
#   test.
class MockContainer(UM.Settings.ContainerInterface.ContainerInterface):
    ##  Initialise a new definition container.
    #
    #   The container will have the specified ID and all metadata in the
    #   provided dictionary.
    def __init__(self, id, metadata):
        self._id = id
        self._metadata = metadata

    ##  Gets the ID that was provided at initialisation.
    #
    #   \return The ID of the container.
    def getId(self):
        return self._id

    ##  Gets all metadata of this container.
    #
    #   This returns the metadata dictionary that was provided in the
    #   constructor of this mock container.
    #
    #   \return The metadata for this container.
    def getMetaData(self):
        return self._metadata

    ##  Gets a metadata entry from the metadata dictionary.
    #
    #   \param key The key of the metadata entry.
    #   \return The value of the metadata entry, or None if there is no such
    #   entry.
    def getMetaDataEntry(self, entry, default = None):
        if entry in self._metadata:
            return self._metadata[entry]
        return default

    ##  Gets a human-readable name for this container.
    #
    #   \return Always returns "MockContainer".
    def getName(self):
        return "MockContainer"

    ##  Get the value of a container item.
    #
    #   Since this mock container cannot contain any items, it always returns
    #   None.
    #
    #   \return Always returns None.
    def getValue(self, key):
        pass

    ##  Serializes the container to a string representation.
    #
    #   This method is not implemented in the mock container.
    def serialize(self):
        raise NotImplementedError()

    ##  Deserializes the container from a string representation.
    #
    #   This method is not implemented in the mock container.
    def deserialize(self, serialized):
        raise NotImplementedError()

@pytest.fixture
def container_registry():
    Resources.addSearchPath(os.path.dirname(os.path.abspath(__file__)))
    UM.Settings.ContainerRegistry._ContainerRegistry__instance = None # Reset the private instance variable every time
    UM.PluginRegistry.PluginRegistry.getInstance().removeType("settings_container")

    return UM.Settings.ContainerRegistry.getInstance()

##  Tests the creation of the container registry.
#
#   This is tested using the fixture to create a container registry.
#
#   \param container_registry A newly created container registry instance, from
#   a fixture.
def test_create(container_registry):
    assert container_registry != None

##  Individual test cases for test_findDefinitionContainers.
#
#   Each entry has a descriptive name for debugging.
#   Each entry also has a list of "containers", each of which is an arbitrary
#   dictionary of metadata. Each dictionary MUST have an ID entry, which will be
#   taken out and used as ID for the container.
#   Each entry also has a "filter" dictionary, which is used as filter for the
#   metadata of the containers.
#   Each entry also has an "answer", which is a list of dictionaries again
#   representing the containers that must be returned by the search.
test_findDefinitionContainers_data = [
    {
        "name": "No containers",
        "containers": [

        ],
        "filter": { "id": "a" },
        "result": [
            # Empty.
        ]
    },
    {
        "name": "Single ID match",
        "containers": [
            { "id": "a" },
            { "id": "b" }
        ],
        "filter": { "id": "a" },
        "result": [
            { "id": "a" }
        ]
    },
    {
        "name": "Double ID match",
        "containers": [
            { "id": "a" },
            { "id": "b" },
            { "id": "a" }
        ],
        "filter": { "id": "a" },
        "result": [
            { "id": "a" },
            { "id": "a" }
        ]
    },
    {
        "name": "Multiple constraints",
        "containers": [
            { "id": "a", "number": 1, "bool": False },
            { "id": "b", "number": 2, "bool": False },
            { "id": "c", "number": 2, "bool": True },
            { "id": "d", "number": 2, "bool": False }
        ],
        "filter": { "number": 2, "bool": False },
        "result": [
            { "id": "b", "number": 2, "bool": False },
            { "id": "d", "number": 2, "bool": False }
        ]
    },
    {
        "name": "Mixed Type",
        "containers": [
            { "id": "a", "number": 1, "mixed": "z" },
            { "id": "b", "number": 1, "mixed": 9 },
            { "id": "c", "number": 2, "mixed": 9 }
        ],
        "filter": { "number": 1, "mixed": 9 },
        "result": [
            { "id": "b", "number": 1, "mixed": 9 }
        ]
    }
]


##  Tests the findDefinitionContainers function.
#
#   \param container_registry A new container registry from a fixture.
#   \param data The data for the tests. Loaded from
#   test_findDefinitionContainers_data.
@pytest.mark.parametrize("data", test_findDefinitionContainers_data)
def test_findDefinitionContainers(container_registry, data):
    for container in data["containers"]: # Fill the registry with mock containers.
        container_id = container["id"]
        del container["id"]
        mock_container = MockContainer(container_id, container)
        container_registry._containers.append(mock_container) # TODO: This is a private field we're adding to here...

    results = container_registry.findDefinitionContainers(data["filter"]) # The actual function call we're testing.

    assert len(results) == len(data["result"]) # Verify we do not get more or less results than expected

    matches = 0
    for result in results: # Go through all results and match them with our expected data
        for required in list(data["result"]): # Iterate over a copy of the list so we do not modify the original data
            if "id" in required:
                # Special casing for id since that is not in the metadata
                if result.getId() != required["id"]:
                    continue
                del required["id"] # Remove id from the expected metadata since it is not part of metadata

            if result.getMetaData() == required:
                # If the metadata matches, we know this entry is valid.
                # Note that this requires specifying all metadata in the expected results.
                matches += 1
                break # Break out of the loop since we have a valid match

    assert matches == len(data["result"])

##  Tests the loading of containers into the registry.
#
#   \param container_registry A new container registry from a fixture.
def test_load(container_registry):
    container_registry.load()

    definitions = container_registry.findDefinitionContainers({ "id": "single_setting" })
    assert len(definitions) == 1

    definition = definitions[0]
    assert definition.getId() == "single_setting"

    definitions = container_registry.findDefinitionContainers({ "author": "Ultimaker" })
    assert len(definitions) == 3

    ids_found = []
    for definition in definitions:
        ids_found.append(definition.getId())

    assert "metadata" in ids_found
    assert "single_setting" in ids_found
    assert "inherits" in ids_found
