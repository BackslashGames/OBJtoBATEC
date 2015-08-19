# OBJtoBATEC
a file created by OtherOS of BackslashGames written in python to convert a .obj to a batec.txt to be used in OtherOS's game HyperFlux (currently no link) 
go to BackslashGames.github.io to download the required file(s)
#limitations
currently you need to build your file in sketchup between 1000 and 9999 on all axis. this should be fixed in a later version
you shouldnt bother texturing any of the surfaces in sketchup. faces are interperated as crosses from corner points.
# Instructions
[note: there is an easier to understand version on the website as well as a link to HyperFlux (probably)]
1. export an .obj from Google Sketchup using TIG's OBJExporter (found on Sketchup's plugin website)
2. open the .obj in a text editor and copy the all of the section with lines starting with "v" into a file called input.txt
3. open input.txt and use the "replace" function (in most text editors) to replace all "v"'s with empty space
4. place the input.txt in the same folder as OBJtoBATEC and then run OBJtoBATEC you should now have 2 extra files in your folder one called "output" and one called "LengthID"
5. open up HyperFlux press q type "load" type "a" and copy the contents of output.txt into the box. and press enter the loader will exit
6. press "q" again and type "load" this time type "l" and type the number on the list of the file you just added. it eill open the decompiler and ask you for the LengthID, simply enter the last number in the file named "LengthID" and it will continue to decompile. once it finishes (becomes inactive) press x and it will exit.
7. currently to see your import press q and type "test" the import should load as a series of crosses (instead of faces) and you have succesfully converted an OBJ into HyperFlux!
#please notify me if you find any problems with the code.
