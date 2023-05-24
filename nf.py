a=["pythonintroquiz","pythonsyntaxquiz","pythonvariablesquiz","pythoncommentsquiz","pythondatatypesquiz","pythonoperatorsquiz","pythonlistsquiz","pythontuplesquiz","pythonsetsquiz","pythondictionariesquiz","pythonifelsequiz","pythonwhilequiz","pythonforquiz","pythonclassquiz","pythonobjectquiz","pythoninheritancequiz","pythonpolymorphismquiz"]
b=[" Intro "," Program"," cout"," cin"," endl"," Variable"," Data types"," Keywords"," Operators"," Identifiers"," Expression "," Control Statement "," if-else"," switch"," For Loop"," While Loop"," Do-While Loop"," Break Statement"," Continue Statement"," Goto Statement"," Comments "," Functions "," FunctionsCall by value & reference"," Recursion"," Storage Classes "," Arrays "," Pointers "," Pointers"," sizeof() operator"," Array of Pointers"," Void Pointer"," References"," Function Pointer"," Memory Management "," Object ","Class "," OOPs Concepts"," Object Class"," Constructor"," Copy Constructor"," Destructor"," this Pointer"," static"," Structs"," Enumeration"," Friend Function"," Math Functions "," Inheritance "," Inheritance"," Aggregation "," Polymorphism"," Overloading"," Overriding"," Virtual Function "," Abstraction "," Interfaces"," Data Abstraction "," Namespaces "," Strings "," Exceptions "," Exception Handling"," try-catch"," User-Defined "," Templates ","Signal Handling "," File and Stream "," getline"]
#c=["HTML-Overview" ,"HTML-Basic Tags" ,"HTML-Elements" ,"HTML-Attributes" ,"HTML-Formatting" ,"HTML-Phrase Tags" ,"HTML-Meta Tags" ,"HTML-Comments" ,"HTML-Images" ,"HTML-Tables" ,"HTML-Lists" ,"HTML-Text Links" ,"HTML-Image Links" ,"HTML-Email Links" ,"HTML-Frames" ,"HTML-Iframes" ,"HTML-Blocks" ,"HTML-Backgrounds" ,"HTML-Colors" ,"HTML-Fonts" ,"HTML-Forms" ,"HTML-Embed Multimedia" ,"HTML-Marquees" ,"HTML-Header" ,"HTML-Style Sheet" ,"HTML-Javascript" ,"HTML-Layouts"]
c=["CSS-Introduction","CSS-Syntax","CSS-Inclusion","CSS-Measurement Units","CSS-Colors","CSS-Backgrounds","CSS-Fonts","CSS-Text","CSS-Images","CSS-Links","CSS-Tables","CSS-Borders","CSS-Margins","CSS-Lists","CSS-Padding","CSS-Cursors","CSS-Outlines","CSS-Dimension","CSS-Scrollbars","CSS Advanced","CSS-Visibility","CSS-Positioning","CSS-Layers","CSS-Pseudo Classes","CSS-Pseudo Elements","CSS-@ Rules","CSS-Text Effects","CSS-Media Types","CSS-Paged Media","CSS-Aural Media","CSS-Printing","CSS-Layouts","CSS-Validations"]
#<li><a href="pythonintro.html">Intro</a></li>
#for i in (a):
#    with open(i+'.js', 'w') as fp:
#        pass
for i in (c):
    with open(i+'.html', 'w') as fp:
        pass
    with open(i+'quiz'+'.html', 'w') as fp:
        pass
    with open(i+'quiz'+'.js', 'w') as fp:
        pass
for i in (c):
    print("<li><a href=\"",end="")
    print(i+'.html'+"\"",end="")
    print(">"+i+"</a></li>")
print("</ul><ul>")
for i in (c):
    print("<li><a href=\"",end="")
    print(i+'quiz'+'.html'+"\"",end="")
    print(">"+i+"Quiz</a></li>")
