## Make Red Hat Free Again

As explained at https://sfconservancy.org/blog/2023/jun/23/rhel-gpl-analysis/, Red Hat is widely known for getting around the GPL license by making refusing to do business with anyone who exercises their GPL rights! However, they also have free trials available, so I was able to obtain their source code nonetheless!

I uploaded their full source code ISO image at https://archive.org/details/rhel-9.4-source-dvd. This repository is dedicated to storing their individual packages, in decompressed form, for easy viewing with Github's code viewer.

I'm not a lawyer, but I believe that this code can be used in other open source programs, subject to the terms of the GPL v2, the EULA, and the individual licenses in each package.

**This package is intended as an easily accessible reference point, but not recommended for compiling**. Due to numourous edge cases (needing to manually decrypt individual folders, Git modifying the line endings of binary files, NTFS possibly replacing special characters in file names) this repo is far from identical to the original source code. If you would like to download and compile a package, I recommend downloading the individual package's .src.rpm file from https://ia800304.us.archive.org/view_archive.php?archive=/2/items/rhel-9.4-source-dvd/rhel-9.4-source-dvd.iso, then extracting it using 7-zip. If you choose to distribute it, please read the EULA (especially section 2), the GPLv2, and any licenses included in the .src.rpm files.

TODO:
- Replace all tarballs with decompressed folders (feel free to open issues requesting specific packages)
    - Please note that I intend to occassionally force-push during this process, for the purpose of saving storage. If you want the compressed archives, please use the archive.org link above
    - frequently run `find -name .gitignore -execdir rename -i .gitignore ".gitignore.disabled by gamer191" .gitignore \;` to disable all gitignore files
- Add files currently listed in .gitignore (read that file for more information)

PS: I'm aware that similar projects exist, such as git.rockylinux.org. The purpose of this project is too:
- Store all Red Hat's code on Github, so it can be easily viewed and copied by other GPL projects, and so it can be easily analysed
- To raise awareness that Red Hat's code is available (legally)

Please send DMCA takedown requests to 68otepg8@duck.com