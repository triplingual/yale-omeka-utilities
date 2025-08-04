echo "Opening the first one takes a moment"
/Applications/Firefox.app/Contents/MacOS/firefox --new-window https://triptronix.net/omekas/admin
echo "Press any key when the site is loading properly"
read -s -n 1
echo "Opening additonal sites now"
open -a Firefox https://triptronix.net/omekas/s/browse-yul-exhibits/
open -a Firefox https://triptronix.net/omekas/s/theme-topnav-test/
open -a Firefox https://triptronix.net/omekas/s/theme-sidenav-test/
open -a Firefox https://onlineexhibits.library.yale.edu/s/100-years-women-ysm/ # (existing topnav example in Prod)
open -a Firefox https://onlineexhibits.library.yale.edu/s/50-years-of-women-s-varsity-athletics-at-yale-a-historic-retrospective # (existing sidenav example in Prod)
open -a Firefox https://onlineexhibits.library.yale.edu/admin
open -a Firefox https://onlineexhibits-test.library.yale.edu/s/100-years-women-ysm/ # (existing topnav example in Test)
open -a Firefox https://onlineexhibits-test.library.yale.edu/s/50-years-of-women-s-sports-at-yale-an-historic-restrospective/ # (existing sidenav example in Test)
open -a Firefox https://onlineexhibits-test.library.yale.edu/admin
