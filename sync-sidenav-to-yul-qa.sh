echo
echo "Dry run of syncing local version of Side Nav Omeka theme with Triptronix"
echo "Note this does not check which git branch is checked out locally"
echo
rsync -auvn --delete --exclude .DS_Store --exclude README.md --exclude .git /Users/trip/Coding/omekaverse/Exhibits_2019_Theme_SideNav onlineexhibitions-qa:~

echo
echo "These are the files that will be copied to or deleted from Triptronix"
read -p "Proceed? " resp1
case $resp1 in
	[yY]|'' ) continue;;
	[nN]* ) echo "exiting"; exit;;
	* ) echo "Must have y/n as response. Exiting."; exit;; 
esac

rsync -auv --delete --exclude .DS_Store --exclude README.md --exclude .git /Users/trip/Coding/omekaverse/Exhibits_2019_Theme_SideNav onlineexhibitions-qa:~
