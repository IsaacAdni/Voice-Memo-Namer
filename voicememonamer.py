import os
import plistlib

with open('AssetManifest.plist', 'rb') as ffp:
     bigPlist = plistlib.load(ffp)
     
for file in os.listdir('.'):
     filename = os.fsdecode(file)
     if filename.endswith(".m4a"):
         rawNumber = filename[:-4]
         plistPath = rawNumber + ".composition/manifest.plist"
         voiceMemoName = ""
         try:
             with open(plistPath, 'rb') as fp:
                 pl = plistlib.load(fp)
             try:   
                 voiceMemoName = pl["RCSavedRecordingTitle"]
                 newName = rawNumber + " - " + voiceMemoName + ".m4a"
                 try:
                     os.rename(filename, newName)
                     print("Succesfully added title '" + voiceMemoName + "' to Voice Memo '" + rawNumber + "'")
                 except:
                     print("FAILED RENAMING FILE *" + rawNumber + "*")
             except:
                 print("ERROR: Voice Memo '" + rawNumber + "' has no title")
         except:
             try:   
                 voiceMemoName = bigPlist[filename]['name']
                 newName = rawNumber + " - " + voiceMemoName + ".m4a"
                 try:
                     os.rename(filename, newName)
                     print("Succesfully added title '" + voiceMemoName + "' to Voice Memo '" + rawNumber + "'")
                 except:
                     print("FAILED RENAMING FILE *" + rawNumber + "*")
             except:
                  print("ERROR: Voice Memo '" + rawNumber + "' has no title")
     else:
         continue
