
#find trunks
find . -type d -iname trunk > /tmp/find-trunk.txt &
#filter paths
cat /tmp/find-trunk.txt | sed 's/\.\(.*\)\/trunk/\1/' > /tmp/paths.tst
# to make script
# sed 's/\.\(.*\)\/trunk/grep -v \1 \| \\/' > /tmp/filter.sh
# edit /tmp/filter.sh
