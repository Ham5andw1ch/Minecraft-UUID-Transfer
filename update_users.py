import sys
import json
import os
import shutil
if len(sys.argv) < 4:
    print("Invalid syntax! Format: python update_users.py new_usercache old_usercache world_folder")
    sys.exit(0)


else:
    new_json_file = open(sys.argv[1],'r',encoding='utf-8-sig')
    data_new = json.load(new_json_file)
    old_json_file = open(sys.argv[2],'r',encoding='utf-8-sig')
    data_old = json.load(old_json_file)

    for p in data_new:
        print("Checking: " + p['name'] + "\n")

        for q in data_old:
            if p['name'] == q['name']:
                #if os.path.isdir("Vowel Gang"):
                ext = [("playerdata",".dat"),("advancements",".json"),("stats",".json")]
                for e in ext:
                    if not os.path.isdir(sys.argv[3] + "/backup"):
                        print("Backup directory doesn't exist. Creating one at: ./" + sys.argv[3] + "/backup\n")
                        os.mkdir(sys.argv[3] + "/backup")
                    if not os.path.isdir(sys.argv[3] + "/backup/" + e[0]):
                        os.mkdir(sys.argv[3] + "/backup/" + e[0])

                    if os.path.exists(sys.argv[3] + "/" + e[0] + "/" + q['uuid'] + e[1]):
                        print("Backing up " + p['name'] + "'s new " +e[0] + " at : ./" +sys.argv[3] + "/backup/" + e[0] +"/" + q['uuid'] + e[1] )
                        shutil.copy(sys.argv[3] +"/" + e[0] +"/" + q['uuid'] + e[1], sys.argv[3] + "/backup/" + e[0] +"/" + q['uuid'] + e[1])

                        if os.path.exists(sys.argv[3] +"/" + e[0] +"/" + p['uuid'] + e[1]):
                            print("Backing up " + p['name'] + "'s old " +e[0] + " at : ./" +sys.argv[3] + "/backup/" + e[0] +"/" + p['uuid'] + e[1] )
                            shutil.move(sys.argv[3] +"/" + e[0] +"/" + p['uuid'] + e[1], sys.argv[3] + "/backup/" + e[0] +"/" + p['uuid'] + e[1])

                        print("Restoring " + p['name'] + "'s old " + e[0])
                        os.rename(sys.argv[3] +"/" + e[0] +"/" + q['uuid'] + e[1],sys.argv[3] +"/" + e[0] +"/" + p['uuid'] + e[1])
                        print("")
    print("Done!")

                    



