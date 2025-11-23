import os
import json
#! add file.close to all of te other thingies
def Setup():
    abspath = os.path.dirname(os.path.abspath(__file__))
    dataPath = os.path.join(abspath, 'data')
    presetNamesPath = os.path.join(abspath, 'data/PresetNames.json')
    presetRenameContentPath = os.path.join(abspath, 'data/presetRenamecontent.txt')
    presetRenameNumPath = os.path.join(abspath, 'data/presetRenameNum.txt')
    SettingsPath = os.path.join(abspath, 'data/Settings.json')
    if not os.path.isdir(dataPath):
        os.mkdir(dataPath)
    if not os.path.isfile(SettingsPath):
        print('setup')
        with open(SettingsPath, 'x') as f:
            baseSettings = {
                'theme': 'dark',
                'notifs': 'True',
                'show-intro': 'True',
            }
            json.dump(baseSettings, f)
        f.close()
    if not os.path.isfile(presetRenameContentPath):
        open(presetRenameContentPath, 'x')
    if not os.path.isfile(presetRenameNumPath):
        open(presetRenameNumPath, 'x')
    if not os.path.isfile(presetNamesPath):
        File = open(presetNamesPath, 'w')
        File.close()
        DataFile = open(presetNamesPath, 'w')
        names = {
            "Preset1Name": "Preset 1",
            "Preset2Name": "Preset 2",
            "Preset3Name": "Preset 3",
            "Preset4Name": "Preset 4",
            "Preset5Name": "Preset 5",
            "Preset6Name": "Preset 6",
            "Preset7Name": "Preset 7",
            "Preset8Name": "Preset 8",
            "Preset9Name": "Preset 9",
            "Preset10Name": "Preset 10",
        }
        compiledNames = (json.dumps(names))
        DataFile.write(compiledNames)
        DataFile.close()