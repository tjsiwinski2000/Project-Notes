     //JSON.parse converts JSON to OBJ
      //restablish OBJ var 'score' on each load
      //OBJ DNE -> "||" -> set default values
      let score = JSON.parse(localStorage.getItem('score')) || {
        wins: 0,
        losses: 0,
        ties: 0
      };
    
     /* the initiliaztion below is no longer necessary due to above snippet after "||"
      if (!score){
        score = { 
          wins: 0,
          losses: 0,
          ties: 0
        }
      }*/

      // Display score at the start of playing.
      updateScoreElement();
        
      console.log(localStorage.getItem('score'));
      function playGame(playerMove){
        const computerMove=pickComputerMove();
        let result=''
        if (playerMove === 'scissors')
        {
          if (computerMove === 'rock'){
            result='You lose.';
          } else if (computerMove === 'paper'){
            result='You win.';
          } else if (computerMove === 'scissors'){
            result='tie';
          }
        } else if (playerMove === 'paper') {
          if (computerMove === 'rock'){
            result='You win.';
          } else if (computerMove === 'paper'){
            result='tie';
          } else if (computerMove === 'scissors'){
            result='You lose.';
          }
        }  else if (playerMove === 'rock'){
            if (computerMove === 'rock'){
                  result='tie';
            } else if (computerMove === 'paper'){
                  result='You lose.';
            } else if (computerMove === 'scissors'){
                  result='You win.';
            }
          }     
      if (result === 'You win.'){
        score.wins +=1;
      } else if (result === 'You lose.'){
        score.losses +=1;
      } else if (result === 'tie'){
        score.ties += 1;
      }
      
      // JSON.stringify converts OBJECT to JSON 
      // JSON can be stored in localStorage
      localStorage.setItem('score', JSON.stringify(score));

      updateScoreElement();
      document.querySelector('.js-result')
        .innerHTML=result;
      
      document.querySelector('.js-moves')
        .innerHTML=`You
      <img src ="images/${playerMove}-emoji.png" 
      class = "move-icon">
      <img src = "images/${computerMove}-emoji.png"
      class="move-icon" >
      Computer`

      console.log(result);
      } //playGame

    
      function updateScoreElement() {
        document.querySelector('.js-score')
        .innerHTML=`Wins: ${score.wins}, Losses: ${score.losses}, Ties: ${score.ties}`;
      }

      function pickComputerMove(){
        const randomNumber=Math.random();
        let computerMove='';
        if(randomNumber >= 0 && randomNumber < 1/3){
          computerMove ='rock';
        } 
        else if (randomNumber >= 1/3 && randomNumber < 2/3)
        {
          computerMove ='paper';
        } 
        else {
          computerMove ='scissors';
        }
        return computerMove;
      }
       