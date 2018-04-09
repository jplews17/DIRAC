""" This is a test of the creation of the pilot wrapper
"""

# pylint: disable=protected-access, invalid-name, no-self-use

import os
import base64
import bz2

import unittest

from DIRAC.WorkloadManagementSystem.Utilities.PilotWrapper import pilotWrapperScript


class PilotWrapperTestCase(unittest.TestCase):
  """ Base class for the Agents test cases
  """

  def setUp(self):
    pass

  def tearDown(self):
    pass


class PilotWrapperTestCaseCreation(PilotWrapperTestCase):

  def test_scriptEmpty(self):
    """ test script creation
    """
    res = pilotWrapperScript()

    print res
    # no assert as it makes little sense

  def test_scriptoptions(self):
    """ test script creation
    """

    res = pilotWrapperScript(
        pilotFilesCompressedEncodedDict={'dirac-install.py': 'someContentOfDiracInstall',
                                         'someOther.py': 'someOtherContent'},
        pilotOptions=['-c 123', '--foo bar'])

    print res
    # no assert as it makes little sense

  def test_scriptReal(self):
    """ test script creation
    """
    diracInstall = os.path.join(os.getcwd(), 'Core/scripts/dirac-install.py')
    with open(diracInstall, "r") as fd:
      diracInstall = fd.read()
    diracInstallEncoded = base64.b64encode(bz2.compress(diracInstall, 9))
    diracPilot = os.path.join(os.getcwd(), 'WorkloadManagementSystem/PilotAgent/dirac-pilot.py')
    with open(diracPilot, "r") as fd:
      diracPilot = fd.read()
    diracPilotEncoded = base64.b64encode(bz2.compress(diracPilot, 9))

    res = pilotWrapperScript(
        pilotFilesCompressedEncodedDict={'dirac-install.py': diracInstallEncoded,
                                         'dirac-pilot.py': diracPilotEncoded},
        pilotOptions=['-c 123', '--foo bar'])

    print res
    # no assert as it makes little sense


#############################################################################
# Test Suite run
#############################################################################


if __name__ == '__main__':
  suite = unittest.defaultTestLoader.loadTestsFromTestCase(PilotWrapperTestCase)
  suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(PilotWrapperTestCaseCreation))
  testResult = unittest.TextTestRunner(verbosity=2).run(suite)

# EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#
