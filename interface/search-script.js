var _prevIndex = 0;
var _nextIndex = 0;
var _resultsPerPage = 10;
var _pageNumber = 1;
var _keywords = ""
//_curindex one's a hacky solution for the elastic search engine. easier than figuring out dsl syntax for doing from in elastic
var _curIndex = 0;
var pid = 'Not set';
curtask = -1;

var fulltasks = ["Stel dat u een onderzoek voorbereid voor een project over fietsgedrag in Utrecht. Is er bij collega's iets bekend over het fietsgebruik van niet-Westerse allochtonen?", "Stel dat u het aantrekkelijk wil maken voor bedrijven om te vestigen in een bepaalde wijk. Hebben collega's data over het aantal bedrijven en het aantal arbeidsplaatsen in de verschillende wijken van Utrecht? Weten ze waarom bedrijven voor deze plekken kiezen?", "Stel dat u een nieuwe speelplek kunt laten bouwen, en wil controleren of er genoeg belangstelling voor is. Is er bij collega's iets bekend over hoeveel kinderen er zijn in de wijk Overvecht, en of we meer jonge huishoudens kunnen verwachten in de toekomst?", "Stel dat u Utrecht aantrekkelijker wilt maken voor toeristen. Weten collega's hoeveel overnachtigen toeristen jaarlijks maken in Utrecht? Waarom kiezen toeristen voor Utrecht?", "Als u een woning koopt zit er een anti-speculatiebeding op om te voorkomen dat mensen huizen kopen om ze vervolgens door te verkopen. Welke collega's weten hoe effectief deze maatregel blijkt te zijn om huizen meer betaalbaar te maken?", "Stel dat u beleid wilt maken om gezond gedrag te stimuleren in  de wijk Leidsche Rijn. U weet dat collega's in een andere wijk hierin succesvol waren. Welke collega's kunnen u uitleggen hoe de Wijkaanpak Overvecht bedacht is?", "Stel dat u de tijdlijn wil schetsen van de bouw van de Uithoflijn, vanaf de planning tot de huidige status. Wie kan u hierbij helpen?", "Stel dat u wilt weten of corona invloed gaat hebben een bouwproject. Wie kan u vertellen of corona invloed heeft op de bouwplannen Zorgcentrum Rosendael?"]

$(function ()
{
    $('#btnSearch').show().click(function () { console.log('btnsearch'); Search($("#txtSearchTerm").val(), $("#engine").val(), $("#retrievalunit").val(), 0, $("#rank").val());});
    $('#lnkPrev').click(function () { Search($("#txtSearchTerm").val(), $("#engine").val(), $("#retrievalunit").val(), -1), $("#rank").val(); });
    $('#lnkNext').click(function () { Search($("#txtSearchTerm").val(), $("#engine").val(), $("#retrievalunit").val(), 1, $("#rank").val());  });
});


//let user confirm they want to leave
//if this returns a string, the user will get a message. do not trigger if the user is performing a query!
var querying = false; //set to true when performing a query - used for warning user when they're closing a window for other reasons than querying

//called onsubmit
function querie(){
    querying = true
}

//called on Search()
function unquerie(){
    querying = false
}



var _engine = "se"
var _retrievalunit = "ru"
var _ranker = "doc"

function Search(term, engine, ru, direction, rank)
{
	var startIndex = 1;
    unquerie()

	if (direction === -1)
	{
		startIndex = _prevIndex; 
		_pageNumber--;
	}
	if (direction === 1)
	{
		startIndex = _nextIndex; 
		_pageNumber++;
	}
	if (direction === 0)
	{
		startIndex = 1; 
		_pageNumber = 1;
	}	
	
	_curIndex = startIndex

	//legacy code: in an old project we also wanted to try google search in soe ways 
	//if google.. 
	if(engine == "g" || engine == "g2"){

		searchKey = mGoogleCustomSearchKeyAll
		if(engine == "g2")
			searchKey = mGoogleCustomSearchKeyiBabs
		var url = "https://www.googleapis.com/customsearch/v1?key="
		+ mGoogleApiKey + "&num=" + _resultsPerPage + "&cx=" + searchKey + "&start=" + startIndex + "&q=" + escape(term) + "&gl=NL&callback=?";
			

		_engine = "g"
	}
	else if(engine == "expert"){
		console.log("Before the expert call")
		_engine = "expert"
        _ru = ru
        _rank = rank

        
        if(rank == "exp" || rank == 'can')
            var url = "http://localhost:8000/queryme/search_exp/" + "?query=" + escape(term) + "&start=" + (startIndex - 1)

        //else: document search
        else
            var url = "http://localhost:8000/queryme/search/" + "?query=" + escape(term) + "&start=" + (startIndex - 1)
        //console.log('here')
        //console.log(url)
	}
	else if(engine == "poc"){
		console.log("Before the PoC call")
		_engine = "poc"
		var url = "http://localhost:8000/queryme/search/" + "?query=" + escape(term) + "&start=" + (startIndex - 1)
	}
	//deprecated: sort by relevancy using oris
	else{
		console.log('Before ORIS call')
		var url = "https://api.openraadsinformatie.nl/v0/utrecht/search" + "?query=" + escape(term) //+ "?size=" + _resultsPerPage + "?from=" + startIndex
		_engine = "o"
//		url = "http://api.openraadsinformatie.nl/v0/utrecht/search?query=de"
	}
	console.log('test2')
	_keywords = term.split(" ")
	$.getJSON(url, '', SearchCompleted);

}

function getPreview(str, keywords){
	str = str.substring(0,500)
	var regKey = keywords[0]
	for(i = 1; i < keywords.length; i++)
		regKey += "|" + keywords[i]
//	var regKey = "hello"
	
	var chunks = str.split(/[.?!]/).filter(function(n) {
		var re = new RegExp(regKey,"i");
		return re.test(n);// /hello/i.test(n);
	});
	console.log(regKey)
	console.log('preview');
	console.log(chunks);
}

function simplePreview(str, keywords){
	console.log('one')
	//only consider the words in the fisrt 500 letters
	fulltext = str.replace('\n'," ").split(" ")
//	console.log(fulltext)
	//find the first occurrence of a keyword, and show 10 words before and 10 words after
	for(ii=0;ii < fulltext.length; ii++){
		for(z = 0; z < keywords.length; z++){
			if(fulltext[ii] === keywords[z]){
				sentence = ""
				//go 10 words before and after the keyword
				for(jj=ii-10; jj < ii+10; jj++){
					if(jj < 0)
						jj = 0
					if(jj == ii)
						sentence += "<b>"
					sentence += fulltext[jj] + " "
					if(jj == ii)
						sentence += "</b>"
				}
				return '.. ' + sentence + ' ..'
			}
		}
	}
	//none found, return first sentence
	return fulltext.slice(0,20).join(" ") + ' ..'
}

function parseiBabs(events, keywords){
	console.log('iBABS')
	results = []
	for(i = 0; i < events.length; i++){
		newresult = {
			"title": events[i].classification + " " + events[i].name,
			"documents": [{}]
		}
		for(j = 0; j < events[i].sources.length; j++){
			newresult.documents.push({
				"title": events[i].sources[j].note,
				"url": events[i].sources[j].url,
				"preview": simplePreview(events[i].sources[j].description, keywords)
				//"preview": "unavailable"//getPreview(events[i].sources[j].description, keywords),
			})
		}
		results.push(newresult)
//		console.log(newresult)
	}
	return results
}


//If using candidate-based interface and eitehr doc or can ranking, each candidate fires a second query to get matching documents
//Those results are parsed here 
function DocsCompleted(response)
{
    //console.log('interpreting docs per candidate')
    //console.log(response.results)
    results = response.results
    console.log(results)
    
    //Very rarely we retrieve a candidate who did not write any documents about the query (it might find them by name).  e.g. ranking=can ru=can q=addink, and rank=can ru=doc q=addink
    //if this is the case we should ignore this author in the interface.
    if(response.results.hits[0] !== undefined){
        author = response.results.hits[0].author
          
        //the html code that will fill the documents panel
        html_auth = ""
        
        //How many documents are we displaying?
        //max 3 for candidate interface
        nr = 3
        //max 1 for documents interface
        if (_ru == 'doc')
            nr = 1
        
        if(results.numresults < nr)
            nr = results.numresults
            
        for (var i = 0; i < nr; i++){
            var item = results.hits[i];
            itemloc = 'C:/Users/Allemaal/Desktop/expertsearch/prepindex/docs/' + item.docid + '.pdf' //'C:/Users/tmsch/Desktop/expert-search/prepindex/docs/' + item.docid + '.pdf'
            
            var ititle = item.title.match(/.{1,63}/g)
//            if (! ititle.includes(" ")){
//            ititle = ititle.
            for (var j = 0; j < ititle.length; j++)
                if (! ititle[j].includes(" "))
                    ititle[j] += " "
            
            ititle = ititle.join("<br> ")
//            ititle = ititle
            
            //console.log(item.preview)
            //var iprev = item.preview.match(/[\s\S]{1,70}/g)
            //for (var j = 0; j < iprev.length; j++)
            //    iprev[j] = iprev[j].trim()
            
            //iprev = iprev.join("<br>&nbsp")
            
//            > 65)
  //              ititle = ititle.substring(0, 65) + " " + ititle.substring(65, ititle.length)
            
            url = itemloc + "' id='" + item.docid
            html_auth += "<p style='padding-left: 4px;'><a class='searchLink' target='_blank' onclick='logclick(\"" + item.docid + "\")' onauxclick='logclick(\"" + item.docid + "\")' href='" + url + "'> " + ititle + "</a>&nbsp;&nbsp;&nbsp;<a class='mlt'></a><br></p>" + "<div style='padding-left: 4px;'>" + item.preview + "</div>"

            if (i + 1 < nr)
                html_auth += "<hr style='height=1px;border-style: none none dotted none; border-width: 1px;'>"
        }
        a = "#" + author.split(' ').join('').split('.').join('')
        //console.log('looking for' + a)
        //console.log($(a).val())
        $(a).html(html_auth)
        //Also store number of results (for logging)
        $(a).attr('nr', nr)
        
        //anchor unhide here
        $(a).parent().show()

        
    //    console.log($("#" + author.split(' ').length)
      //  console.log("#" + author.split(' ').join(''))
        //console.log(html_auth)
    }
}

//All queries fired end up here to parse the results
function SearchCompleted(response)
{
	//console.log('hi')
	console.log('search completed')
	console.log(_engine)
	console.log(response)
    console.log(rank)
	
		
	if(_engine == "g" || _engine == "g2"){
		var html = "";
		$("#searchResult").html("");

		if (response.items == null)
		{
			$("#searchResult").html("No matching pages found");
			return;
		}

		if (response.items.length === 0)
		{
			$("#searchResult").html("No matching pages found");
			return;
		}

		
		$("#searchResult").html("Around " + response.queries.request[0].totalResults + " pages found for <b>" +response.queries.request[0].searchTerms+ "</b><br><br>");
		
		//store the number of results 
		logNumResults(response.queries.request[0].totalResults, 0)


		if (response.queries.nextPage != null)
		{
			_nextIndex = response.queries.nextPage[0].startIndex;
			$("#lnkNext").show();
		}
		else
		{
			$("#lnkNext").hide();
		}

		if (response.queries.previousPage != null)
		{
			_prevIndex = response.queries.previousPage[0].startIndex;
			$("#lnkPrev").show();
		}
		else
		{
			$("#lnkPrev").hide();
		}

		if (response.queries.request[0].totalResults > _resultsPerPage){
			$("#lblPageNumber").show().html(_pageNumber);
		}
		else{
			$("#lblPageNumber").hide();
		}

		console.log('check me')
		console.log(response)
		for (var i = 0; i < response.items.length; i++){
			var item = response.items[i];
			var title = item.htmlTitle;
        
			html += "<p><a class='searchLink' href='" + item.link + "'> " + title + "</a><br>";
			//if we recognise pdf/word, add a date
	//		snippetdate = item.pagemap.metatags[0].creationdate
//			console.log(snippetdate)
		//	console.log('snip')
		//	if(typeof(snippetdate) != 'undefined')
		//		html += snippetdate.substring(8, 10) + " " + snippetdate.substring(6,8) + " " + snippetdate.substring(2,6) + ' .. '
			
			html += item.htmlSnippet + "<p>";
			//html += item.link + "<br>"// + " - <a href='http://www.google.com/search?q=cache:"+	item.cacheId+":"+item.displayLink+"'>Cached</a>";
			html += "</p><p>";
		}
	}
	// CODE FOR EXPERT SEARCH RESULTS
	else if (_engine=="expert"){
		console.log('interpreting expert search results')
		html = ""
		results = response.results
        
		if (results.numresults === 0)
		{
			$("#searchResult").html("No matching pages found");
			return;
		}
		
		$("#searchResult").html(results.numresults + " results found for <b>" + _keywords.join(" ") + "</b><br><br>");
		
		//$("#output").html(html)
		
		//store the number of results 
		logNumResults(results.numresults, results.numresults)

		//TODO not working, because &from is not parsed as a thing different from a query
		//-> do we ever need it for our usecase?
		//	 supposed to skip ahead if we do indeed skip the first x if we do ?from=x
		//console.log(from)
		//console.log('milestone')
        
        
        
		if (results.numresults > 10)
		{
			_nextIndex = _curIndex + _resultsPerPage;
			$("#lnkNext").show();
		}
		else
		{
			$("#lnkNext").hide();
		}
		
		if (_pageNumber > 1)
		{


	//		we forgot to implement this, and instead manually corrected after the experiment. TODO
			_prevIndex = _curIndex - _resultsPerPage;//response.queries.previousPage[0].startIndex;
			$("#lnkPrev").show();
		}
		else
		{
			$("#lnkPrev").hide();
		}
		
		if (_pageNumber > 1){
			$("#lblPageNumber").show().html(_pageNumber);
		}
		else{
			$("#lblPageNumber").hide();
		}
        
        
        //Now choose what type of interface we show / what is hte retrieval unit: author or document?
        authors_found = ""
        if(_ru == "exp"){
            //$("#searchResult").html("About to go down");
            
            for (var i = 0; i < results.hits.length && i < _resultsPerPage; i++){
                //This is the first candidate
                var item = results.hits[i];
                
                
                //If ranking is documents + interface is candidates, we can have the same candidate multiple times
                //Filter candidates that recurr
                if (!authors_found.includes(item.author)){
                    authors_found += item.author
              
                    //console.log(item)
                    
                    //should the checkbox be marked?
                    checked = ''
                    if (localStorage.getItem(pid+'toggles'+curtask).includes(item.author))//.split(' ').join('').split('.').join(''))
                        checked = ' checked'
                        
                    //background-color: #edf4ff;
                    //Create expert panel
                    html += "<div style='display:none; overflow:auto; background-color:#edf4ff;'><div style='width: 30%; float:left;'><p>&nbsp;<b>Auteur</b>: " + item.author + "<br>&nbsp;<b>Portefeuilles</b>: " + item.expertise + "<br>&nbsp;<b>Contact</b>: Private<br>&nbsp;<b>I might ask them</b>: <input type='checkbox' resrnk=" + i + " id='" + item.author + "' class='regular-checkbox' onclick='toggleAuthor(this)' onauxclick='toggleAuthor(this)' " + checked + " /></p></div>"

                    //We now query the top5 documents per expert
                    //At this point, we add a div with the id of the author. Once the appropriate JSON request is
                    //completed, we fill it with the results

                    //create document panel
                    html += "<div id='" + item.author.split(' ').join('').split('.').join('') + "' style='width: 70%; min-height: 100px; float:right; background-color:#f5f9ff; border-style: none none none dotted; border-width: 1px;'></div>";
                    
                    //fire json request
                    //console.log(item.author)
                    $.getJSON("http://localhost:8000/queryme/search_auth_docs/" + "?query=" + escape(_keywords.join(" ")) + "&start=" + escape(item.author), '', DocsCompleted);
    //                $.getJSON("http://localhost:8000/queryme/search/" + "?query=" + escape(item.author), '', function() {
    //                DocsCompleted() });
                                 
                    html += "</div>"
                    
                    html += "<hr style='border:none'><hr><hr style='border:none'>";
                }
            }
            
            
        }
        //document search interface
        else{
            console.log('document search ui')
		
        
		
            //console.log(results.hits)
            //console.log(results.numresults)
            for (var i = 0; i < results.hits.length && i < _resultsPerPage; i++){
                var item = results.hits[i];
                //console.log(item)
                //if(item == undefined)
                //	alert(i)
                
                // sometimes there's an 'undefined' result we hsould skip
                if(item !== undefined){
                    
                    //if ru = doc   rank = cand   then we have to do an extra step now
                    // to translate the retrieved candidate to their top relevant doc
                    if(_rank == "exp" || _rank =='can'){
//                        alert(item.author.split(' ').join('').split('.').join(''))
                        //doc panel placeholder
                        html += "<div style='overflow:auto; background-color:#edf4ff;'><div id='" + item.author.split(' ').join('').split('.').join('') + "' style='width: 70%; min-height: 120px; float:left; background-color:#f5f9ff; border-style: none dotted none none; border-width: 1px;'>";
                        $.getJSON("http://localhost:8000/queryme/search_auth_docs/" + "?query=" + escape(_keywords.join(" ")) + "&start=" + escape(item.author), '', DocsCompleted);
                    }
                    else{
                        
                        var title = item.title;
                        if (!title.includes(" ") & title.length > 65)
                            title = title.substring(0, 65) + " " + title.substring(65, title.length)
                
                        //temp fix
                        itemloc = 'C:/Users/Allemaal/Desktop/expertsearch/prepindex/docs/' + item.docid + '.pdf'// 'C:/Users/tmsch/Desktop/expert-search/prepindex/docs/' + item.docid + '.pdf'
                        
                        //background-color: #edf4ff;
                        //create document panel of search result
                        html += "<div style='overflow:auto; background-color:#edf4ff;'><div style='width: 70%; min-height: 120px; float:left; background-color:#f5f9ff; border-style: none dotted none none; border-width: 1px;'><p style=' '><a class='searchLink' target='_blank' onclick='logclick(\"" + item.docid + "\")' onauxclick='logclick(\"" + item.docid + "\")' href='" + itemloc + "' id='" + item.docid + "'> " + title + "</a>&nbsp;&nbsp;&nbsp;<a class='mlt'></a><br>";
                    
                        html += item.preview;
                    }
                        
                    //should the checkbox be marked?
                    checked = ''
                    if (localStorage.getItem(pid+'toggles'+curtask).includes(item.author))
                        checked = ' checked'
                        
                    //Add expert panel
                    html += "</p></div><div style='width: 30%; float:right; padding-left: 4px;'><p><b>Auteur</b>: " + item.author + "<br><b>Portefeuilles</b>: " + item.expertise + "<br><b>Contact</b>: Private<br><b>I might ask them</b>: <input type='checkbox' onclick='toggleAuthor(this)' onauxclick='toggleAuthor(this)'" + checked + " resrnk=" + i + " id='" + item.author + "' class='regular-checkbox' /></p></div>"
    //				Portefeuilles staan even uit, omdat ik ze niet heb
    //html += "</p></div><div style='width: 30%; float:right;'><p>&nbsp;<b>Auteur</b>: " + item.author + "<br>&nbsp;<b>Portefeuilles</b>: Zaken doen<br>&nbsp;<b>Contact</b>: Private</p></div>"
                                 
                    html += "</div>"
                    
                    html += "<hr>";
                    
                }
            }
        }
		
		
	}
	else if (_engine=="poc"){
//		results = parsePoC(response.events, _keywords)
		console.log('interpreting poc')
		html = ""
		results = response.results
		
		if (results.numresults === 0)
		{
			$("#searchResult").html("No matching pages found");
			return;
		}
		
		$("#searchResult").html(results.numresults + " results found for <b>" + _keywords.join(" ") + "</b><br><br>");
		
		//$("#output").html(html)
		
		//store the number of results 
		logNumResults(results.numresults, results.numresults)

		//TODO not working, because &from is not parsed as a thing different from a query
		//-> do we ever need it for our usecase?
		//	 supposed to skip ahead if we do indeed skip the first x if we do ?from=x
		//console.log(from)
		console.log('milestone')
		if (results.numresults > _resultsPerPage)
		{
			_nextIndex = _curIndex + _resultsPerPage;
			$("#lnkNext").show();
		}
		else
		{
			$("#lnkNext").hide();
		}
		
		if (_pageNumber > 1)
		{


	//		TODO same as before with the other _previndex
			_prevIndex = _curIndex - _resultsPerPage;//response.queries.previousPage[0].startIndex;
			$("#lnkPrev").show();
		}
		else
		{
			$("#lnkPrev").hide();
		}
		
		if (_pageNumber > 1){
			$("#lblPageNumber").show().html(_pageNumber);
		}
		else{
			$("#lblPageNumber").hide();
		}
		
		//console.log(results.hits)
		//console.log(results.numresults)
		for (var i = 0; i < results.hits.length && i < _resultsPerPage; i++){
			var item = results.hits[i];
			//if(item == undefined)
			//	alert(i)
			
			// sometimes there's an 'undefined' result that we skip
			
			//NOTE this part of the code was for a proof of concept searhc engine with erfgoed (cultural heritage) data
			if(item !== undefined){
				
				var title = item.title;
        
				//temp fix
				itemloc = 'C:/Users/tmsch/Desktop/werk/erfgoed/erfgoed docs/' + title
				html += "<p><a class='searchLink' href='" + itemloc + "' id='" + item.docid + "'> " + title + "</a>&nbsp;&nbsp;&nbsp;<a class='mlt'></a><br>";
//			html += "<p><a class='searchLink' href='" + item.url + "' id='" + item.docid + "'> " + title + "</a>&nbsp;&nbsp;&nbsp;<a class='mlt'>More like this!</a><br>";
			//<i>" + item.url + "</i><br>
			//if we recognise pdf/word, add a date
	//		snippetdate = item.pagemap.metatags[0].creationdate
//			console.log(snippetdate)
		//	console.log('snip')
		//	if(typeof(snippetdate) != 'undefined')
		//		html += snippetdate.substring(8, 10) + " " + snippetdate.substring(6,8) + " " + snippetdate.substring(2,6) + ' .. '
			
				html += item.preview;
			//html += item.link + "<br>"// + " - <a href='http://www.google.com/search?q=cache:"+	item.cacheId+":"+item.displayLink+"'>Cached</a>";
			
			//mfd more from domain code - disabled for erfgoed
			//html += "<br><a class='mfd' domain='" + item.domain + "'>More from " + item.domain.replace('www.','') + "</a><hr>";
				html += "<hr>";
			}
		}
		
		
	}
	else{
		console.log('te')
		results = parseiBabs(response.events, _keywords)
		console.log('te')
		//clear previous resulst
		html = ""
		
		if (response.events == null || response.events.length === 0)
		{
			$("#searchResult").html("No matching pages found");
			return;
		}
		
		//find number of documents
		numdocs = 0
		for(i = 0; i < response.events.length; i++){
			numdocs += response.events[i].sources.length;
		}
		$("#searchResult").html("Around " + response.meta.total + " results found containing " + numdocs + " documents for <b>" + _keywords + "</b><br><br>");
		
		//store the number of results 
		logNumResults(response.meta.total, numdocs)

		if (response.events.length > _resultsPerPage)
		{
			_nextIndex = startIndex + _resultsPerPage;
			$("#lnkNext").show();
		}
		else
		{
			$("#lnkNext").hide();
		}
		
		if (_pageNumber > 1)
		{
			_prevIndex = response.queries.previousPage[0].startIndex;
			$("#lnkPrev").show();
		}
		else
		{
			$("#lnkPrev").hide();
		}
		
		if (_pageNumber > 1){
			$("#lblPageNumber").show().html(_pageNumber);
		}
		else{
			$("#lblPageNumber").hide();
		}
		
		for (var i = 0; i < results.length; i++){
			html += "<p><p><p><h4><b>" + results[i].title + "</h4></b>"
			for (var j = 1; j < results[i].documents.length; j++){
				html += "<a class='searchLink' " + results[i].documents[j].url + ">" + results[i].documents[j].title + "</a><br>" + results[i].documents[j].preview + "<p><p>"// + results[i].documents[j].preview + "<br><br>"
			
//			<a class='searchLink' href='" + item.link + "'> " + title + "</a><br>"
			
	//		var item = results[i];
		//	var title = item.htmlTitle;
        
//			html += "<p><a class='searchLink' href='" + item.link + "'> " + title + "</a><br>";
	//		html += item.snippet + "<br>";
		//	html += item.link + " - <a href='http://www.google.com/search?q=cache:"+	item.cacheId+":"+item.displayLink+"'>Cached</a></p><p>";
			}
			html += "</p><p>"
		}
		
	}
	$("#output").html(html)
	
	bindClicks();
}

window.onbeforeunload = function(e) {
  if(!querying){
    localStorage.setItem(pid+'logs', localStorage.getItem(pid+'logs') + 'time ' + Date.now() + ' task ' + localStorage.getItem(pid+'curtask') + ' window close?\n')
    return "Do you want to exit this page?";
  }
};

//button to let user start and end tasks. adds markers in logging data so we know when they start/finish
function startTask(startbut){
    //in both cases, remove all checkmarks 
    //uncheck all checkboxes
    $(":checkbox").removeAttr('checked')

    
    
    if(startbut.getAttribute("value") == "Start task"){
        
        //switch button 
        startbut.setAttribute("style", "background-color: #f74040;	color:#fff; border:none; text-align: center;")
        startbut.setAttribute("value", "Stop searching")
        
        logs = localStorage.getItem(pid+'logs');
        hightask = parseInt(localStorage.getItem(pid+'hightask'));
                
        newresult = "time " + Date.now() + " starting task " + hightask + "\n"
        localStorage.setItem(pid+'curtask', hightask);
        localStorage.setItem(pid+'hightask', hightask);
                
        if(logs === null)
            localStorage.setItem(pid+'logs', newresult)
        else
            localStorage.setItem(pid+'logs', logs + newresult)

        localStorage.setItem(pid+'toggles'+hightask, '')
        
        
        //set task text in interface
        console.log(localStorage.getItem(pid+'tasks'))
        t = localStorage.getItem(pid+'tasks')[hightask]
        $('#task').html(fulltasks[parseInt(t)])

        
//        $('.check:button').toggle(function(){
//            alert('hi')
//            $('input:checkbox').attr('checked','checked');
//            $(this).val('uncheck all');
//        },function(){
//            $('input:checkbox').removeAttr('checked');
//            $(this).val('check all');        
  //      })
    }
    else{
        if(confirm("Are you done searching?") == true){
            startbut.setAttribute("style", "background-color: #03fc8c;	color:#fff; border:none; text-align: center;")
            startbut.setAttribute("value", "Start task")
            
            logs = localStorage.getItem(pid+'logs');
            curtask = localStorage.getItem(pid+'curtask');
            hightask = parseInt(localStorage.getItem(pid+'hightask'));
            newresult = "time " + Date.now() + " stopping task " + curtask + "\n";
            
            localStorage.setItem(pid+'curtask', '-1');
            localStorage.setItem(pid+'hightask', '' + (hightask + 1));
            
            if(logs === null)
                localStorage.setItem(pid+'logs', newresult)
            else
                localStorage.setItem(pid+'logs', logs + newresult)
                
            //if we finished the first half of the tasks
            if(hightask == 3){
                
                querie() //call this to avoid 'are you sure you want to leave' pop up
                alert('You finished the first half of the tasks!')
                window.location.reload();
            }
            //if we finished all tasks
            if(hightask == 7){
                alert('You finished all the tasks!')
            }
            
            //set task text in interface
            $('#task').html("Your search task will be here")
        }
    }
}

//nr = number of results for this author
//defaults to 1 (document view)
function toggleAuthor(item){
    //Find author name
    name = item.getAttribute('id')
    
    
    //Find num results in documents panel
    // find by author name
    a = $("#" + name.split(' ').join('').split('.').join(''))
    if(!a)
        alert('something went wrong - could not find panel')
    else{
        nr = parseInt(a.attr('nr'))
        if (! nr)
            nr = 1
    }
    
    
    
    // Log toggle actions in joint log
    logs = localStorage.getItem(pid+'logs');
    curtask = localStorage.getItem(pid+'curtask')

    // Check if this author is toggled on in logs atm
    toggles = localStorage.getItem(pid+'toggles'+curtask)
    if (toggles.includes(name)){
        newresult = "time " + Date.now() + " task " + curtask + " toggle off " + name + " rank " + item.getAttribute('resrnk') + " numresults " + nr + '\n'
        localStorage.setItem(pid+'toggles'+curtask, toggles.replace(name, ""))
        
        //Toggle all instances off in interface (in doc interface the same author is displayed multiple times)
        //alert('removing ' + name)
        console.log($("[id='" + name + "]'"))
        $("[id='" + name + "']").removeAttr('checked')
    }
    else{
        newresult = "time " + Date.now() + " task " + curtask + " toggle on " + name + " rank " + item.getAttribute('resrnk') + " numresults " + nr + '\n'
        localStorage.setItem(pid+'toggles'+curtask, toggles + " " + name)
        
        //Toggle all instances on in interface (in doc interface the same author is displayed multiple times)
        //alert('adding ' + name)
        console.log($("[id='" + name + "']"))
        $("[id='" + name + "']").each(function(){ $(this).prop('checked', true) })
    }
    
    
    if(logs === null)
        localStorage.setItem(pid+'logs', newresult)
    else
        localStorage.setItem(pid+'logs', logs + newresult)
    
    
}

// log clicked result
// NOTE in future work we should update it to remember on what page the user was.. in the experiment, we manually kept track
function logclick(url){
    logs = localStorage.getItem(pid+'logs');
    curtask = localStorage.getItem(pid+'curtask');
    
    newresult = "time " + Date.now() + " task " + curtask + " click " + url + '\n'
    if(logs === null)
        localStorage.setItem(pid+'logs', newresult)
    else
        localStorage.setItem(pid+'logs', logs + newresult)
    
    //change color of URL so user can find it again
    $("#"+url).css('color','purple')
}

function startLogging(id){
    pid = "participant " + id
    
    //if this is the first time for this participant id
    if (localStorage.getItem(pid) === null) {
        name = prompt('What is the name of ' + pid + '?')
        localStorage.setItem(pid, name)
        localStorage.setItem(pid+'curtask', '-1') //set to inactive
        localStorage.setItem(pid+'hightask', '0')
        localStorage.setItem(pid+'logs', '')
        localStorage.setItem(pid+'toggles-1', '')
    }
    
    //test if there is an active task (e.g. reloading the page by doing a new query)
    // if so, set button
    if (localStorage.getItem(pid+'curtask') != '-1'){
        startbut = $('#taskButton')
        startbut.attr("style", "background-color: #f74040;	color:#fff; border:none; text-align: center;")
        startbut.attr("value", "Stop searching")
        
        //set task text in interface
        t = localStorage.getItem(pid+'tasks')[parseInt(localStorage.getItem(pid+'hightask'))]
        $('#task').html(fulltasks[parseInt(t)])
    }
    
    //log that the window was opened
    localStorage.setItem(pid+'logs', localStorage.getItem(pid+'logs') + 'time ' + Date.now() + ' task ' + localStorage.getItem(pid+'curtask') + ' window open?\n')
    
    //double check if tasks were set yet
    if(localStorage.getItem(pid+'tasks') === null) {
        //if we don't recognise task order because it could be because it is a testrun. otherwise, becacuse we haven't set it yet
        if(pid.includes('-')){
            localStorage.setItem(pid+'ranking1', localStorage.getItem('participant 0ranking1'))
            localStorage.setItem(pid+'ranking2', localStorage.getItem('participant 0ranking2'))
            localStorage.setItem(pid+'interfaces', localStorage.getItem('participant 0interfaces'))
            localStorage.setItem(pid+'tasks', localStorage.getItem('participant 0tasks'))
        }
    }

    //test if there are authors who should be toggled on for this task
    //already done when loading checkboxes     
}

function logNumResults(nr,nd){
	console.log('updating numresults')
//    console.log(typeof nr)
//    nr=nr.replace("\n","")
    nr = parseInt(nr)
	//TODO get it 
//	let gett = 
	
    
    //this part not for experiment
	numresults = localStorage.getItem('numresults');
	numresults += Date.now() + " Query " + _keywords.join("-") + " Numresults " + nr + '\n'
	localStorage.setItem('numresults', numresults)
//	gett.then((results) => {
//		numresults = results.numresults
//		numresults.loglines.push(Date.now() + " Query " + _keywords.join("-") + " Numresults " + nr + " Numdocs " + nd)
//		storeLogs();
	//})
    
    //EXPERIMENT log queries
    logs = localStorage.getItem(pid+'logs');
    curtask = localStorage.getItem(pid+'curtask');
    
    newresult = "time " + Date.now() + " task " + curtask + " query " + _keywords.join(" ") + " numresults " + nr + '\n'
    
    if(logs === null)
        localStorage.setItem(pid+'logs', newresult)
    else
        localStorage.setItem(pid+'logs', logs + newresult)
}

/*function storeLogs(){
	let contentToStore = {};
	contentToStore['numresults'] = numresults;
	localStorage.set(contentToStore);
}*/

// Called when html objects for the results are created using the elastic search (other searches dont create the objects)
// call morelikethis function, append top 3 to this result
function bindClicks(){
	console.log('check')
	//more like this button
	$(".mlt" ).click(function() {
		//alert($(this).parent() + " clicked");
		console.log($(this).parent() + " clicked");
		html = "<br><br>"
		htmlreference = $(this)
		
		//Do Elastic mlt query with size 3 for more documents like this
		$.ajax({url: "http://localhost:8000/queryme/recommend" + "?query=" + escape($(this).parent().children("a.searchLink").attr("id")) + "&size=3", success: function(results){
			results = results.results
			//console.log(results.numresults)
			//console.log(results.hits)
			for (var i = 0; results.numresults > 0 && i < results.hits.length; i++){
				var item = results.hits[i];
				var title = item.title;
        
				html += "<p>&nbsp;* <a class='searchLink3' href='" + item.url + "'>" + title + "</a><br>";
				html += item.preview + "<p><p>";
			}
			//html+= "<hr>";
//			$("#div1").html(result);
			console.log(html)
			console.log($(this).parent())
			htmlreference.parent().append(html)

		}});
		
	});
	
	//more from domain button
	$(".mfd" ).click(function() {
		console.log($(this).parent() + " clicked");
		html = "<br><br>"
		htmlreference = $(this)
		
		//Do Elastic query within domain with size 4 (= skip first result, which we already see)
		$.ajax({url: "http://localhost:8000/queryme/domainsearch" + "?query=" + escape(_keywords) + "&size=4&domain=" + htmlreference.attr('domain'), success: function(results){
			results = results.results
			console.log(results.numresults)
			console.log(results.hits)
			for (var i = 0; results.numresults > 0 && i < results.hits.length; i++){
				var item = results.hits[i];
				var title = item.title;
        
				html += "<p>&nbsp;* <a class='searchLink2' href='" + item.url + "'>" + title + "</a><br>";
				html += item.preview + "<p><p>";
			}
			//html+= "<hr>";
//			$("#div1").html(result);
			console.log(html)
			console.log($(this).parent())
			htmlreference.parent().append(html)

		}});
		
	});
	
	
}

function onInstalledNotification(details) {
	//We should store the # results in localStorage.
		//On page start: check if logs already exist
		//On Query(): log new query w results and date.now()
	numresultsQ = localStorage.getItem('numresults');
	var numresults = ""
//	gett.then((results) => {
	if(typeof numresultsQ === "undefined"){
		console.log('initialising numresults')
		numresults = Date.now() + " Storing the number of results per query\n"
		localStorage.setItem('numresults', numresults)
	}
	else{
		console.log('loading numresults')
		numresults = numresultsQ;
	}
	
	//Selects all (i.e. the only) values selected
	$( "#theme" ).change(function() {
		var themec = "";
		$( "select option:selected" ).each(function() {
			themec += $( this ).val() + " ";
		});
		console.log(themec);
		//Tell server to filter on theme, then call search
		$.ajax({url: "http://localhost:8000/queryme/theme" + "?theme=" + themec, success: function(results){
			Search($("#txtSearchTerm").val(), $("#engine").val(), $("#retrievalunit").val(), 0, $("#rank").val())
		}});
	}).trigger( "change" );
	//})
}


//Randomly generated task orders from python shuffle
n = 25
task_order = ['07314625', '15740236', '41605273', '01325746', '30265147', '45760312', '16025734', '30167254', '54326017', '64721503', '60513427', '06324715', '32146057', '21450736', '32461057', '61534720', '02164735', '63157402', '15327460', '42675031', '20174653', '61427053', '42173650', '23701564', '63714520']

interface_order = ['can', 'doc', 'can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can']

ranking1_order = ['can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can']
ranking2_order = ['doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc']

function setTasks(){
    for (let i = 0; i < n; i++) {
        localStorage.setItem('participant ' + i + 'tasks', task_order[i])
        localStorage.setItem('participant ' + i + 'interfaces', interface_order[i])
        localStorage.setItem('participant ' + i + 'ranking1', ranking1_order[i])
        localStorage.setItem('participant ' + i + 'ranking2', ranking2_order[i])
    }
}

//set tasks - doesn't matter that we rewrite this because it's seeded
setTasks()
onInstalledNotification();

