def removetmp():
    import os
    import shutil
    rfiles=["fautofill","fdownloads","fhistory","fkeywords","flogins","ftopsites"]
    for x in rfiles:
        os.remove("/tmp/"+x)
    shutil.rmtree("/tmp/user-profile-images", ignore_errors=True)