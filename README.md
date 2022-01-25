# SafeCopy
Very simple Python script to automatically copy a folder every 15 minutes.

I created it to save my Dark Souls 3 saves, but feel free to use it, modify it!

"original" is where the folder comes from. The last part is the actual folder which will be copied.
"targetpath" is where the folder will be copied. The last part is very important, it will be the name of the your folder (original name will be replaced).

Now, in <code>copytree(original, targetpath + " " + safe_time)</code>, the last part <code> + " " + safe_time</code> adds a space after your folder's name (for me, save) and then the date and hour. It's optionnal and can be deleted. In this case, the folder will just be replaced by the new one, since the name will be the same.

Date/Hour format is line 13:
<code>safe_time = CurDT.strftime("%Y-%m-%d %Hh %Mm %Ss")</code>
You can switch it up however you'd like. Just remember to use characters allowed in folders' names. ( <b>:</b> and <b>/</b> won't work )

The script runs in an endless loop as it is now, and must be turned on and off manually.
