mkdir -p outputs
echo "["$(date +%d-%m-%H:%M:%S)"] Script executed"  >> logs/log.txt
echo "["$(date +%d-%m-%H:%M:%S)"] Starting download of home programmes"  >> logs/log.txt
python3 programmes_downloader.py --config-file ./configs/home.conf --output ./outputs/home.xml
echo "["$(date +%d-%m-%H:%M:%S)"] Download of home programmes finished"  >> logs/log.txt
echo "["$(date +%d-%m-%H:%M:%S)"] Starting download of all programmes"  >> logs/log.txt
python3 programmes_downloader.py --config-file ./configs/all.conf --output ./outputs/all.xml
echo "["$(date +%d-%m-%H:%M:%S)"] Download of all programmes finished"  >> logs/log.txt
