

var quesans_pair = 0;
function submit_prompt(event) {
        //prevents automatic page reloading (what usually happens when form submits)
    event.preventDefault();
    console.log(event)
    var prompt = $('#prompt').val();
    console.log(prompt.trim());
    /*
- have 2 variables, quesans_pair and current height
- when new prompt is added, quesans_pair += 1
- new element for qn and ans, each with id = 'question/ans'+= str(quesans_pair)
- currentheight will += prev ans/question height
- new height will be used to style the top of the block 
- 

    */
    var html_text = ''; 

    if (prompt.trim() !== '') {
        quesans_pair += 1;
        var source = new EventSource("/stream_chatbot/?prompt=" + encodeURIComponent(prompt),
            {withCredentials: true}); 
        
        $('#prompt').val('');
        console.log('EventSource created.');
        var parentElement = document.getElementById('chat_message_space');

        //creat div for prompt
        var question = document.createElement('div');
        question.textContent = prompt;
        question.classList.add('question');
        parentElement.appendChild(question);
        question.id = 'question'+ quesans_pair.toString();
        
        



        //get question height for styling
        console.log('question height:'+ question.offsetHeight);
        //current_height += question.offsetHeight;
        
    

        //create div for reply
        var reply = document.createElement('div');
        reply.textContent = '';
        reply.classList.add('result');
        parentElement.appendChild(reply);
        reply.id = 'result'+quesans_pair.toString();
        //styliing for result
        
        

        source.onmessage = function(event) {
        
        if (event.data == 'finc') {
            //nothing new to add
            
            //console.log(reply.textContent)
            parentElement.appendChild(reply);
            //current_height += reply.offsetHeight;
            source.close();
            console.log('SSE connection closed.');
            
            
        } else {
            //add info to reply
            data = JSON.parse(event.data);
            token = data.content;
            //console.log(token)
            html_text += token;
        
            reply.innerHTML = marked.parse(html_text);
            //console.log(event.data)
            
            //reply.textContent += event.data;
            
            parentElement.scrollTo(0, parentElement.scrollHeight);
            
            
        };
        }
    }
    
}

    
    