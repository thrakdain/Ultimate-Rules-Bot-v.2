import discord
import os

from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('!rulesbot'):
        await message.channel.send('**Commands**\n\n!rulebook\n\n!1.\n\t!1.1\n\t!1.2\n\t!1.3\n\t!1.4\n\t!1.5\n\t!1.6\n\t!1.7\n\t!1.8\n\t!1.9\n\t!1.10\n\t!1.11\n\t!1.12\n\n!2.\n\t!2.1\n\t!2.2\n\t!2.3\n\t!2.4\n\t!2.5\n\t!2.6\n\t!2.7\n\t!3.\n\t!3.1\n\t!3.2\n\t!3.3\n\t!3.4\n\n!4.\n\t!4.1\n\t!4.2\n\t!4.3\n\t!4.4\n\t!4.5\n\n!5.\n\t!5.1\n\t!5.2\n\t!5.3\n\n!6.\n\t!6.1\n\t!6.2\n\t!6.3\n\n!7.\n\t!7.1\n\t!7.2\n\t!7.3\n\t!7.4\n\t!7.5\n\t!7.6\n\t!7.7\n\t!7.8\n\t!7.9\n\t!7.10\n\t!7.11\n\t!7.12\n\n!8.\n\t!8.1\n\t!8.2\n\t!8.3\n\t!8.4\n\t!8.5\n\n!9.\n\t!9.1\n\t!9.2\n\t!9.3\n\t!9.4\n\t!9.5\n\t!9.6\n\n!10.\n\t!10.1\n\t!10.2\n\t!10.3\n\t!10.4\n\t!10.5\n\t!10.6\n\t!10.7\n\n!11.\n\t!11.1\n\t!11.2\n\t!11.3\n\t!11.4\n\t!11.5\n\t!11.6\n\t!11.7\n\t!11.8\n\t!11.9\n\n!12.\n\t!12.1\n\t!12.2\n\t!12.3\n\t!12.4\n\t!12.5\n\t!12.6\n\t!12.7\n\t!12.8\n\t!12.9\n\t!12.10\n\n!13.\n\t!13.1\n\t!13.2\n\t!13.3\n\t!13.4\n\t!13.5\n\t!13.6\n\t!13.7\n\t!13.8\n\t!13.9\n\t!13.10\n\t!13.11\n\t!13.12\n\n!14.\n\t!14.1\n\t!14.2\n\t!14.3\n\t!14.4\n\n!15.\n\t!15.1\n\t!15.2\n\t!15.3\n\t!15.4\n\t!15.5\n\t!15.6\n\t!15.7\n\t!15.8\n\t!15.9\n\t!15.10\n\t!15.11\n\t!15.12\n\t!15.13\n\n!16.\n\t!16.1\n\t!16.2\n\t!16.3\n\n!17.\n\t!17.1\n\t!17.2\n\t!17.3\n\t!17.4\n\t!17.5\n\t!17.6\n\t!71.7\n\t!17.8\n\t!17.9\n\n!18.\n\t!18.1\n\t!18.2\n\t!18.3\n\n!19.\n\t!19.1\n\t!19.2\n\t!19.3\n\n!20.\n\t!20.1\n\t!20.2\n\t!20.3\n\t!20.4\n\n**Fouls, Infractions and Violations**\n\n!dangerous play\n\n!receiving foul\n\n!strip\n\n!blocking\n\n!force-out\n\n!defensive foul\n\n!offensive foul\n\n!indirect foul\n\n!off setting foul\n\n!marking infraction\n\n!fast count\n\n!straddle\n\n!disc space\n\n!wrapping\n\n!double team\n\n!vision\n\n!travel\n\n!pick\n\n!new rules')


    if message.content.startswith('!rulebook'):
        await message.channel.send('1.Spirit of the Game\n\n2.Playing Field\n\n3.Equipment\n\n4.Point, Goal and Game\n\n5.Teams\n\n6.Starting a Game\n\n7.The Pull\n\n8.State of play\n\n9.Stall Count\n\n10.The Check\n\n11.Out-of-Bounds\n\n12. Recievers and Positioning\n\n13.Turnovers\n\n14.Scoring\n\n15.Calling Fouls, Infractions and Violations\n\n16.Continuation after a Call\n\n17.Fouls\n\n18.Infractions and Violations\n\n19.Safety Stoppages\n\n20.Time-Outs')


    if message.content.startswith('!1.'):

        if message.content.startswith('!1.1'):


          if message.content.startswith('!1.10'):
            await message.channel.send('1.10. Calls should be discussed by the players directly involved in the play, and by players who had the best perspective on the play.\n\t1.10.1. If a player who was not directly involved believes that a team-mate has made an incorrect call, or caused a foul or violation, they should inform their team-mate.\n\t1.10.2 Non-players, apart from the captains, should refrain from getting involved. However players may seek other peoples\' perspectives to clarify the rules, and to assist players to make the appropriate call') 

          elif message.content.startswith('!1.11'):
            await message.channel.send('1.11. Players and captains are solely responsible for making and resolving all calls.') 

          elif message.content.startswith('!1.12'):
            await message.channel.send('1.12. If, after discussion, players cannot agree, or it is not clear and obvious:\n\t1.12.1. what occurred in a play, or1.\n\t12.2. what would most likely have occurred in a play, \n\tthe disc must be returned to the last non-disputed thrower.') 

          else:
            await message.channel.send('1.1.  Ultimate is a non-contact, self-officiated sport. All players are responsible for administering and adhering to the rules. Ultimate relies upon a Spirit of the Game that places the responsibility for fair play on every player.')  
        
        elif message.content.startswith('!1.2'):
          await message.channel.send('1.2.  It is trusted that no player will intentionally break the rules; thus there are no harsh penalties for inadvertent breaches, but rather a method for resuming play in a manner which simulates what would most likely have occurred had there been no breach.\n\n\t1.2.1. If there is a deliberate or egregious breach of the rules or Spirit of the Game, the captains should discuss this and determine an appropriate outcome, even if that outcome is not in accordance with a specific rule.')

        elif message.content.startswith('!1.3'):
          await message.channel.send('1.3.  Players   should be mindful of the fact that they are acting as referees in any arbitration between teams. Players must:\n\t1.3.1. know the rules;\n\t1.3.2. be fair-minded and objective;\n\t1.3.3. be truthful;\n\t1.3.4. explain their viewpoint clearly and briefly;\n\t1.3.5. allow opponents a reasonable chance to speak;\n\t1.3.6. consider their opponent’s viewpoint;\n\t1.3.7. use respectful words and body language with consideration of potential cultural differences;\n\t1.3.8. resolve disputes as quickly as possible, using respectful language;\n\t1.3.9. make calls in a consistent manner throughout the game; and\n\t1.3.10. only make a call where a breach is significant enough to make a difference to the outcome of the action.')

        elif message.content.startswith('!1.4'):
          await message.channel.send('1.4. Highly competitive play is encouraged, but should never sacrifice the mutual respect between players, adherence to the agreed-upon rules of the game, player safety or the basic joy of play.')

        elif message.content.startswith('!1.5'):
          await message.channel.send('1.5. The following actions are examples of good Spirit:\n\t1.5.1. retracting a call when you no longer believe the call was correct;\n\t1.5.2. checking in with an opponent on the sideline after a contentious interaction;\n\t1.5.3. complimenting an opponent for good play or Spirit;\n\t1.5.4. introducing yourself to your opponent; and\n\t1.5.5. reacting calmly towards disagreement or provocation.')

        elif message.content.startswith('!1.6'):
         await message.channel.send('1.6. The following actions are clear violations of the Spirit of the Game and must be avoided:\n\t1.6.1. dangerous play and aggressive behaviour;\n\t1.6.2. intentional fouling or other intentional rule breaches;\n\t1.6.3. taunting or intimidating opposing players;\n\t1.6.4. celebrating disrespectfully after scoring;\n\t1.6.5. making calls in retaliation to an opponent’s call;\n\t1.6.6. calling for a pass from an opposition player; and\n\t1.6.7. other win-at-all-costs behaviour.')     

        elif message.content.startswith('!1.7'):
         await message.channel.send('1.7. Teams are guardians of the Spirit of the Game, and must:1.7.1. take responsibility for teaching their players the rules and good Spirit;1.7.2. discipline team-mates who display poor Spirit;1.7.3. provide constructive feedback to other teams about what they are doing well and/or how to improve their adherence to the Spirit of the Game; and1.7.4. call a Spirit Stoppage to address Spirit issues, as appropriate.')    

        elif message.content.startswith('!1.8'):
          await message.channel.send('1.8. In the case where a novice player is involved in a breach and does not know the rules, experienced players should assist to explain the breach.') 

        elif message.content.startswith('!1.9'):
          await message.channel.send('1.9. An experienced player, who offers advice on rules and guides on-field arbitration, may supervise games involving beginners or younger players.')        
        else:
          await message.channel.send('1. Spirit of the Game\n‎‎‏‏‎ ‎')
          await message.channel.send('1.1.  Ultimate is a non-contact, self-officiated sport. All players are responsible for administering and adhering to the rules. Ultimate relies upon a Spirit of the Game that places the responsibility for fair play on every player.\n‎‎‏‏‎ ‎')

          await message.channel.send('1.2.  It is trusted that no player will intentionally break the rules; thus there are no harsh penalties for inadvertent breaches, but rather a method for resuming play in a manner which simulates what would most likely have occurred had there been no breach.\n\n\t1.2.1. If there is a deliberate or egregious breach of the rules or Spirit of the Game, the captains should discuss this and determine an appropriate outcome, even if that outcome is not in accordance with a specific rule.\n‎‎‏‏‎ ')

          await message.channel.send('1.3.  Players should be mindful of the fact that they are acting as referees in any arbitration between teams. Players must:\n\t1.3.1. know the rules;\n\t1.3.2. be fair-minded and objective;\n\t1.3.3. be truthful;\n\t1.3.4. explain their viewpoint clearly and briefly;\n\t1.3.5. allow opponents a reasonable chance to speak;\n\t1.3.6. consider their opponent’s viewpoint;\n\t1.3.7. use respectful words and body language with consideration of potential cultural differences;\n\t1.3.8. resolve disputes as quickly as possible, using respectful language;\n\t1.3.9. make calls in a consistent manner throughout the game; and\n\t1.3.10. only make a call where a breach is significant enough to make a difference to the outcome of the action.\n‎‎‏‏‎ ')

          await message.channel.send('1.4. Highly competitive play is encouraged, but should never sacrifice the mutual respect between players, adherence to the agreed-upon rules of the game, player safety or the basic joy of play.\n‎‎‏‏‎ ')  

          await message.channel.send('1.5. The following actions are examples of good Spirit:\n\t1.5.1. retracting a call when you no longer believe the call was correct;\n\t1.5.2. checking in with an opponent on the sideline after a contentious interaction;\n\t1.5.3. complimenting an opponent for good play or Spirit;\n\t1.5.4. introducing yourself to your opponent; and\n\t1.5.5. reacting calmly towards disagreement or provocation.\n‎‎‏‏‎ ')

          await message.channel.send('1.6. The following actions are clear violations of the Spirit of the Game and must be avoided:\n\t1.6.1. dangerous play and aggressive behaviour;\n\t1.6.2. intentional fouling or other intentional rule breaches;\n\t1.6.3. taunting or intimidating opposing players;\n\t1.6.4. celebrating disrespectfully after scoring;\n\t1.6.5. making calls in retaliation to an opponent’s call;\n\t1.6.6. calling for a pass from an opposition player; and\n\t1.6.7. other win-at-all-costs behaviour.\n‎‎‏‏‎ ') 

          await message.channel.send('1.7. Teams are guardians of the Spirit of the Game, and must:\n\t1.7.1. take responsibility for teaching their players the rules and good Spirit;\n\t1.7.2. discipline team-mates who display poor Spirit;\n\t1.7.3. provide constructive feedback to other teams about what they are doing well and/or how to improve their adherence to the Spirit of the Game; and\n\t1.7.4. call a Spirit Stoppage to address Spirit issues, as appropriate.\n‎‎‏‏‎ ') 

          await message.channel.send('1.8. In the case where a novice player is involved in a breach and does not know the rules, experienced players should assist to explain the breach.\n‎‎‏‏‎ ')

          await message.channel.send('1.9. An experienced player, who offers advice on rules and guides on-field arbitration, may supervise games involving beginners or younger players.\n‎‎‏‏‎ ')

          await message.channel.send('1.10. Calls should be discussed by the players directly involved in the play, and by players who had the best perspective on the play.\n\t1.10.1. If a player who was not directly involved believes that a team-mate has made an incorrect call, or caused a foul or violation, they should inform their team-mate.\n\t1.10.2 Non-players, apart from the captains, should refrain from getting involved. However players may seek other peoples\' perspectives to clarify the rules, and to assist players to make the appropriate call\n‎‎‏‏‎ ') 

          await message.channel.send('1.11. Players and captains are solely responsible for making and resolving all calls.\n‎‎‏‏‎ ') 

          await message.channel.send('1.12. If, after discussion, players cannot agree, or it is not clear and obvious:\n\t1.12.1. what occurred in a play, or1.\n\t12.2. what would most likely have occurred in a play, \n\tthe disc must be returned to the last non-disputed thrower.\n‎‎‏‏‎ ')  



    if message.content.startswith('!2.'):

      if message.content.startswith('!2.1'):
        await message.channel.send('2.1. The playing field is a rectangular area with dimensions and zones as shown on Figure 1 (see above) and should be essentially flat, free of obstructions and afford reasonable player safety. ')  

      elif message.content.startswith('!2.2'):
        await message.channel.send('2.2. The perimeter lines surround the playing field and consist of two (2) sidelines along the length and two (2) endlines along the width.')  

      elif message.content.startswith('!2.3'):   
        await message.channel.send('2.3. The perimeter lines are not part of the playing field.')  

      elif message.content.startswith('!2.4'): 
       await message.channel.send('2.4. The goal lines are the lines that separate the central zone from the end zones and are part of the central zone.')  

      elif message.content.startswith('!2.5'):    
        await message.channel.send('2.5. The brick marks are the intersection of two (2) crossed one (1) metre lines in the central zone, located a distance equal to the length of the end zone away from each goal line, midway between the sidelines.')  

      elif message.content.startswith('!2.6'):   
        await message.channel.send('2.6. Eight brightly-coloured, flexible objects (such as plastic cones) mark the corners of the central zone and the end zones.')  

      elif message.content.startswith('!2.7'):    
        await message.channel.send('2.7. The immediate surroundings of the playing field shall be kept clear of movable objects. If play is obstructed by non-players or objects within three (3) metres of the perimeter line, any obstructed player or thrower in possession may call “Violation”.') 

      else:
        await message.channel.send('2. Playing Field\n‎‎‏‏‎ ‎  ‎')        
        await message.channel.send('2.1. The playing field is a rectangular area with dimensions and zones as shown on Figure 1 (see above) and should be essentially flat, free of obstructions and afford reasonable player safety.\n‎‎‏‏‎ ‎ ')  
        await message.channel.send('2.2. The perimeter lines surround the playing field and consist of two (2) sidelines along the length and two (2) endlines along the width.\n‎‎‏‏‎ ‎')  
        await message.channel.send('2.3. The perimeter lines are not part of the playing field.\n‎‎‏‏‎ ‎')  
        await message.channel.send('2.4. The goal lines are the lines that separate the central zone from the end zones and are part of the central zone.\n‎‎‏‏‎ ‎')
        await message.channel.send('2.5. The brick marks are the intersection of two (2) crossed one (1) metre lines in the central zone, located a distance equal to the length of the end zone away from each goal line, midway between the sidelines.\n‎‎‏‏‎ ‎')  
        await message.channel.send('2.6. Eight brightly-coloured, flexible objects (such as plastic cones) mark the corners of the central zone and the end zones.\n‎‎‏‏‎ ‎')  
        await message.channel.send('2.7. The immediate surroundings of the playing field shall be kept clear of movable objects. If play is obstructed by non-players or objects within three (3) metres of the perimeter line, any obstructed player or thrower in possession may call “Violation”.\n‎‎‏‏‎ ‎') 
   


    if message.content.startswith('!3.'):

      if message.content.startswith('!3.1'):
        await message.channel.send('3.1. Any flying disc acceptable to both captains may be used. ')  

      elif message.content.startswith('!3.2'):
        await message.channel.send('3.2. WFDF may maintain a list of approved discs recommended for use.')  

      elif message.content.startswith('!3.3'):
        await message.channel.send('3.3. Each player must wear a uniform that distinguishes their team. ')  

      elif message.content.startswith('!3.4'):
        await message.channel.send('3.4. No player may wear items of clothing or equipment that reasonably could harm the wearer or other players, or impede an opponent\'s ability to play.  ')  
      
      else:
        await message.channel.send('3. Equipment\n‎‎‏‏‎ ‎  ‎')
        await message.channel.send('3.1. Any flying disc acceptable to both captains may be used.\n‎‎‏‏‎ ‎ ')  
        await message.channel.send('3.2. WFDF may maintain a list of approved discs recommended for use.\n‎‎‏‏‎ ‎')  
        await message.channel.send('3.3. Each player must wear a uniform that distinguishes their team.\n‎‎‏‏‎ ‎ ')
        await message.channel.send('3.4. No player may wear items of clothing or equipment that reasonably could harm the wearer or other players, or impede an opponent\'s ability to play. \n‎‎‏‏‎ ‎ ') 



    if message.content.startswith('!4.'):

      if message.content.startswith('!4.1'):
        await message.channel.send('4.1. A game consists of a number of points.  Each point ends with the scoring of a goal.')  

      elif message.content.startswith('!4.2'):
        await message.channel.send('4.2. A game is finished and won by the first team to score fifteen (15) goals.')  

      elif message.content.startswith('!4.3'):   
        await message.channel.send('4.3. A game is separated into two (2) periods of play, called halves.  Half time occurs when a team first scores eight (8) goals.')  

      elif message.content.startswith('!4.4'): 
       await message.channel.send('4.4. The first point of each half starts when the half starts.')  

      elif message.content.startswith('!4.5'):    
        await message.channel.send('4.5. After a goal is scored, and the game has not been won or half time has not been reached:\n\t4.5.1. the next point starts immediately;\n\t4.5.2. the teams switch the end zone that they are defending; and\n\t4.5.3. the team that scored becomes defence and pulls next.')  

      else:
        await message.channel.send('4. Point, Goal and Game\n‎‎‏‏‎ ‎  ‎')        
        await message.channel.send('4.1. A game consists of a number of points.  Each point ends with the scoring of a goal.\n‎‎‏‏‎ ‎ ')  
        await message.channel.send('4.2. A game is finished and won by the first team to score fifteen (15) goals.\n‎‎‏‏‎ ‎')  
        await message.channel.send('4.3. A game is separated into two (2) periods of play, called halves.  Half time occurs when a team first scores eight (8) goals.\n‎‎‏‏‎ ‎')  
        await message.channel.send('4.4. The first point of each half starts when the half starts.\n‎‎‏‏‎ ‎')
        await message.channel.send('4.5. After a goal is scored, and the game has not been won or half time has not been reached:\n\t4.5.1. the next point starts immediately;\n\t4.5.2. the teams switch the end zone that they are defending; and\n\t4.5.3. the team that scored becomes defence and pulls next.\n‎‎‏‏‎ ‎')  



    if message.content.startswith('!5.'):

      if message.content.startswith('!5.1'):
        await message.channel.send('5.1. Each team will put a maximum of seven (7) players and a minimum of five (5) players on the field during each point.')  

      elif message.content.startswith('!5.2'):
        await message.channel.send('5.2. Each team must designate a captain and a spirit captain to represent the team.')  

      elif message.content.startswith('!5.3'):   
        await message.channel.send('5.3. A team may make unlimited substitutions after a goal is scored and before their team signals readiness for the pull.')  

      else:
        await message.channel.send('5. Teams\n‎‎‏‏‎ ‎  ‎')        
        await message.channel.send('5.1. Each team will put a maximum of seven (7) players and a minimum of five (5) players on the field during each point.\n‎‎‏‏‎ ‎ ')  
        await message.channel.send('5.2. Each team must designate a captain and a spirit captain to represent the team\n‎‎‏‏‎ ‎')  
        await message.channel.send('5.3. A team may make unlimited substitutions after a goal is scored and before their team signals readiness for the pull.\n‎‎‏‏‎ ‎')



    if message.content.startswith('!6.'):

      if message.content.startswith('!6.1'):
        await message.channel.send('6.1. Representatives of the two teams fairly determine which team first chooses either:\n\t6.1.1. whether to receive or throw the initial pull; or\n\t6.1.2. which end zone they will initially defend.')  

      elif message.content.startswith('!6.2'):
        await message.channel.send('6.2. The other team is given the remaining choice.')  

      elif message.content.startswith('!6.3'):   
        await message.channel.send('6.3. At the start of the second half, these initial selections are switched.')  

      else:
        await message.channel.send('6. Starting a Game\n‎‎‏‏‎ ‎  ‎')        
        await message.channel.send('6.1. Representatives of the two teams fairly determine which team first chooses either:\n\t6.1.1. whether to receive or throw the initial pull; or\n\t6.1.2. which end zone they will initially defend.\n‎‎‏‏‎ ‎ ')  
        await message.channel.send('6.2. The other team is given the remaining choice.\n‎‎‏‏‎ ‎')  
        await message.channel.send('6.3. At the start of the second half, these initial selections are switched.\n‎‎‏‏‎ ‎')



    if message.content.startswith('!7.'):

        if message.content.startswith('!7.1'):


          if message.content.startswith('!7.10'):
            await message.channel.send('7.10. If the disc initially contacts the playing field and never becomes out-of-bounds, the thrower must establish a pivot point where the disc stops, even if that pivot point is in their defending end zone.') 

          elif message.content.startswith('!7.11'):
            await message.channel.send('7.11. If the disc initially contacts the playing field and then becomes out-of-bounds without contacting an offensive player, the thrower must establish a pivot point where the disc first crossed the perimeter line, or the nearest location in the central zone if that pivot point would be in their defending end zone. \n\t7.11.1. If the disc does contact an offensive player before it becomes out-of-bounds the thrower must establish a pivot point where the disc first crossed the perimeter line, even if that pivot point is in their defending end zone.') 

          elif message.content.startswith('!7.12'):
            await message.channel.send('7.12. If the disc contacts the out-of-bounds area without first touching the playing field or an offensive player, the thrower may establish a pivot point either at the brick mark closest to their defending end zone, or at the location on the central zone closest to where the disc went out-of-bounds (Section 11.8).  The binding brick option must be signalled before the disc is picked up, by any offensive player fully extending one arm overhead and calling "brick".') 

          else:
            await message.channel.send('7.1. At the start of the game, after half-time or after a score, play commences with a throw by the defence, called a "pull". \n\t7.1.1. Teams must prepare for the pull without unreasonable delay.')  
        
        elif message.content.startswith('!7.2'):
          await message.channel.send('7.2. The pull may be made only after both teams have signalled their readiness by having the puller and a player on offence raise a hand above their head.')

        elif message.content.startswith('!7.3'):
          await message.channel.send('7.3. After signalling readiness all offensive players must stand with one foot on their defending goal line without changing location relative to one another until the pull is released.')

        elif message.content.startswith('!7.4'):
          await message.channel.send('7.4. After signalling readiness all defensive players must keep their feet entirely behind the vertical plane of the goal line until the pull is released.')

        elif message.content.startswith('!7.5'):
          await message.channel.send('7.5. If a team breaches 7.3 or 7.4 the opposing team may call a violation (“offside”). This must be called before the offence touches the disc (7.8 still applies).\n\t7.5.1. If the defence chooses to call offside, the thrower must establish a pivot point as per 7.9, 7.10, 7.11, or 7.12 and then play restarts as soon as possible as if a time-out had been called at that location.\n\t7.5.2. If the offence chooses to call offside, they must let the disc hit the ground untouched and then resume play as if a brick has been called (no check is required).')

        elif message.content.startswith('!7.6'):
         await message.channel.send('7.6. As soon as the disc is released, all players may move in any direction.')     

        elif message.content.startswith('!7.7'):
         await message.channel.send('7.7. No player on the defensive team may touch the disc after a pull until a member of the offensive team contacts the disc or the disc hits the ground.')    

        elif message.content.startswith('!7.8'):
          await message.channel.send('7.8. If an offensive player, in-bounds or out-of-bounds, touches the disc before it hits the ground, and the offensive team fails to subsequently establish possession, that is a turnover (a “dropped pull”).') 

        elif message.content.startswith('!7.9'):
          await message.channel.send('7.9. If an offensive player catches the pull and subsequently establishes possession, they must establish a pivot point at the location on the playing field nearest to where possession is established, even if that pivot point is in their defending end zone.')        
        else:
          await message.channel.send('7. The Pull\n‎‎‏‏‎ ‎')
          await message.channel.send('7.1. At the start of the game, after half-time or after a score, play commences with a throw by the defence, called a "pull". \n\t7.1.1. Teams must prepare for the pull without unreasonable delay.\n‎‎‏‏‎ ‎')

          await message.channel.send('7.2. The pull may be made only after both teams have signalled their readiness by having the puller and a player on offence raise a hand above their head.\n‎‎‏‏‎ ')

          await message.channel.send('7.3. After signalling readiness all offensive players must stand with one foot on their defending goal line without changing location relative to one another until the pull is released.\n‎‎‏‏‎ ')

          await message.channel.send('7.4. After signalling readiness all defensive players must keep their feet entirely behind the vertical plane of the goal line until the pull is released.\n‎‎‏‏‎ ')  

          await message.channel.send('7.5. If a team breaches 7.3 or 7.4 the opposing team may call a violation (“offside”). This must be called before the offence touches the disc (7.8 still applies).\n\t7.5.1. If the defence chooses to call offside, the thrower must establish a pivot point as per 7.9, 7.10, 7.11, or 7.12 and then play restarts as soon as possible as if a time-out had been called at that location.\n\t7.5.2. If the offence chooses to call offside, they must let the disc hit the ground untouched and then resume play as if a brick has been called (no check is required).\n‎‎‏‏‎ ')

          await message.channel.send('7.6. As soon as the disc is released, all players may move in any direction.\n‎‎‏‏‎ ') 

          await message.channel.send('7.7. No player on the defensive team may touch the disc after a pull until a member of the offensive team contacts the disc or the disc hits the ground. \n‎‎‏‏‎ ') 

          await message.channel.send('7.8. If an offensive player, in-bounds or out-of-bounds, touches the disc before it hits the ground, and the offensive team fails to subsequently establish possession, that is a turnover (a “dropped pull”).\n‎‎‏‏‎ ')

          await message.channel.send('7.9. If an offensive player catches the pull and subsequently establishes possession, they must establish a pivot point at the location on the playing field nearest to where possession is established, even if that pivot point is in their defending end zone.\n‎‎‏‏‎ ')

          await message.channel.send('7.10. If the disc initially contacts the playing field and never becomes out-of-bounds, the thrower must establish a pivot point where the disc stops, even if that pivot point is in their defending end zone.\n‎‎‏‏‎ ') 

          await message.channel.send('7.11. If the disc initially contacts the playing field and then becomes out-of-bounds without contacting an offensive player, the thrower must establish a pivot point where the disc first crossed the perimeter line, or the nearest location in the central zone if that pivot point would be in their defending end zone. \n\t7.11.1. If the disc does contact an offensive player before it becomes out-of-bounds the thrower must establish a pivot point where the disc first crossed the perimeter line, even if that pivot point is in their defending end zone.\n‎‎‏‏‎ ') 

          await message.channel.send('7.12. If the disc contacts the out-of-bounds area without first touching the playing field or an offensive player, the thrower may establish a pivot point either at the brick mark closest to their defending end zone, or at the location on the central zone closest to where the disc went out-of-bounds (Section 11.8).  The binding brick option must be signalled before the disc is picked up, by any offensive player fully extending one arm overhead and calling "brick". \n‎‎‏‏‎ ')  



    if message.content.startswith('!8.'):

      if message.content.startswith('!8.1'):
        await message.channel.send('8.1. Play is \'dead\', and no turnover is possible:\n\t8.1.1. After the start of a point, until the pull is released;\n\t8.1.2. When the disc must be carried to the pivot location after the pull or after a turnover, until a pivot point is established;\n\t8.1.3. After a call which stops the play or any other stoppage, until the disc is checked in; or\n\t8.1.4. After a disc hits the ground, until possession is established by the appropriate team.\n\t8.1.5. Players are allowed to move during dead play (unless specified otherwise). ')  

      elif message.content.startswith('!8.2'):
        await message.channel.send('8.2. Play that is not dead is "live".')  

      elif message.content.startswith('!8.3'):   
        await message.channel.send('8.3. The thrower may not transfer possession of the disc during dead play to another player.')  

      elif message.content.startswith('!8.4'): 
       await message.channel.send('8.4. Any player may attempt to stop a disc from rolling or sliding after it has hit the ground.\n\t8.4.1. If, in attempting to stop such a disc, a player significantly alters the disc’s position, the opposition may request that the pivot point be established at the location where the disc was contacted.')  

      elif message.content.startswith('!8.5'):    
        await message.channel.send('8.5. After a turnover, and after the pull, an offensive player must move at walking pace or faster to directly retrieve the disc and establish a pivot point.\n\t8.5.1. In addition to 8.5, after a turnover the offence must put the disc into play within the following time limits, if the disc did not become out-of-bounds, and the disc\'s location is: \n\t\t8.5.1.1. in the central zone – within ten (10) seconds of the disc coming to rest.\n\t\t8.5.1.2. in an end zone – within twenty (20) seconds of the disc coming to rest.\n\t8.5.2. If the offence breaches 8.5, or 8.5.1, the defence may give a verbal warning (“Delay of Game” or using a pre-stall) or may call a “Violation”.\n\t\t8.5.2.1. If, after a warning, the offence continues to breach 8.5, or 8.5.1, then 9.3.1 does not apply and the marker may commence the stall count.')  

      else:
        await message.channel.send('8. State of Play\n‎‎‏‏‎ ‎  ‎')        
        await message.channel.send('8.1. Play is \'dead\', and no turnover is possible:\n\t8.1.1. After the start of a point, until the pull is released;\n\t8.1.2. When the disc must be carried to the pivot location after the pull or after a turnover, until a pivot point is established;\n\t8.1.3. After a call which stops the play or any other stoppage, until the disc is checked in; or\n\t8.1.4. After a disc hits the ground, until possession is established by the appropriate team.\n\t8.1.5. Players are allowed to move during dead play (unless specified otherwise).\n‎‎‏‏‎ ‎ ')  
        await message.channel.send('8.2. Play that is not dead is "live".\n‎‎‏‏‎ ‎')  
        await message.channel.send('8.3. The thrower may not transfer possession of the disc during dead play to another player.\n‎‎‏‏‎ ‎')  
        await message.channel.send('8.4. Any player may attempt to stop a disc from rolling or sliding after it has hit the ground.\n\t8.4.1. If, in attempting to stop such a disc, a player significantly alters the disc’s position, the opposition may request that the pivot point be established at the location where the disc was contacted.\n‎‎‏‏‎ ‎')
        await message.channel.send('8.5. After a turnover, and after the pull, an offensive player must move at walking pace or faster to directly retrieve the disc and establish a pivot point.\n\t8.5.1. In addition to 8.5, after a turnover the offence must put the disc into play within the following time limits, if the disc did not become out-of-bounds, and the disc\'s location is: \n\t\t8.5.1.1. in the central zone – within ten (10) seconds of the disc coming to rest.\n\t\t8.5.1.2. in an end zone – within twenty (20) seconds of the disc coming to rest.\n\t8.5.2. If the offence breaches 8.5, or 8.5.1, the defence may give a verbal warning (“Delay of Game” or using a pre-stall) or may call a “Violation”.\n\t\t8.5.2.1. If, after a warning, the offence continues to breach 8.5, or 8.5.1, then 9.3.1 does not apply and the marker may commence the stall count.\n‎‎‏‏‎ ‎')



    if message.content.startswith('!9.'):

      if message.content.startswith('!9.1'):
        await message.channel.send('9.1. The marker administers a stall count on the thrower by announcing “Stalling” and then counting from one (1) to ten (10).  The interval between the start of each number in the stall count must be at least one (1) second.')  

      elif message.content.startswith('!9.2'):
        await message.channel.send('9.2. The stall count must be clearly communicated to the thrower.')  

      elif message.content.startswith('!9.3'):   
        await message.channel.send('9.3. The marker may only start and continue a stall count when: \n\t9.3.1. Play is live, or until a pivot is established after a turnover;\n\t9.3.2. They are within three (3) metres of the thrower\'s pivot point, or the pivot location if the thrower is not at the location; and\n\t9.3.3. All defenders are legally positioned (Section 18.1).')  

      elif message.content.startswith('!9.4'): 
       await message.channel.send('9.4. If the marker moves beyond the appropriate three (3) metre radius, or a different player becomes the marker, the stall count must be restarted at "Stalling one (1)".')  

      elif message.content.startswith('!9.5'):    
        await message.channel.send('9.5. After a stoppage in play the stall count is resumed as follows: \n\t9.5.1. After an accepted breach by the defence the stall count restarts at "Stalling one (1)".\n\t9.5.2. After an accepted breach by the offence the stall count restarts at maximum nine(9).\n\t9.5.3. After a contested stall-out the stall count restarts at "Stalling eight (8)".\n\t9.5.4. After all other calls, including "pick", the stall count restarts at maximum six (6). However: \n\t\t9.5.4.1. If there is a call involving the thrower, and a separate receiving breach, and the disc is returned to the thrower, the stall count is resumed based on the outcome of the call involving the thrower. \n\t\t9.5.4.2. If there is a violation called related to The Check (Section 10), the stall count resumes at the same count that was determined prior to that violation. ')  

      elif message.content.startswith('!9.6'):   
        await message.channel.send('9.6. To restart a stall count “at maximum n”, where “n” is determined by 9.5.2, 9.5.4, or 20.3.6, means the following:\n\t9.6.1. If "x" is the last agreed number fully uttered prior to the call, then the stall count resumes at “Stalling (x plus one)” or “Stalling n”, whichever of those two numbers is lower.')  

      else:
        await message.channel.send('9. Stall Count\n‎‎‏‏‎ ‎  ‎')        
        await message.channel.send('9.1. The marker administers a stall count on the thrower by announcing “Stalling” and then counting from one (1) to ten (10).  The interval between the start of each number in the stall count must be at least one (1) second.\n‎‎‏‏‎ ‎ ')  
        await message.channel.send('9.2. The stall count must be clearly communicated to the thrower.\n‎‎‏‏‎ ‎')  
        await message.channel.send('9.3. The marker may only start and continue a stall count when: \n\t9.3.1. Play is live, or until a pivot is established after a turnover;\n\t9.3.2. They are within three (3) metres of the thrower\'s pivot point, or the pivot location if the thrower is not at the location; and\n\t9.3.3. All defenders are legally positioned (Section 18.1).\n‎‎‏‏‎ ‎')  
        await message.channel.send('9.4. If the marker moves beyond the appropriate three (3) metre radius, or a different player becomes the marker, the stall count must be restarted at "Stalling one (1)".\n‎‎‏‏‎ ‎')
        await message.channel.send('9.5. After a stoppage in play the stall count is resumed as follows: \n\t9.5.1. After an accepted breach by the defence the stall count restarts at "Stalling one (1)".\n\t9.5.2. After an accepted breach by the offence the stall count restarts at maximum nine(9).\n\t9.5.3. After a contested stall-out the stall count restarts at "Stalling eight (8)".\n\t9.5.4. After all other calls, including "pick", the stall count restarts at maximum six (6). However: \n\t\t9.5.4.1. If there is a call involving the thrower, and a separate receiving breach, and the disc is returned to the thrower, the stall count is resumed based on the outcome of the call involving the thrower. \n\t\t9.5.4.2. If there is a violation called related to The Check (Section 10), the stall count resumes at the same count that was determined prior to that violation.\n‎‎‏‏‎ ‎')  
        await message.channel.send('9.6. To restart a stall count “at maximum n”, where “n” is determined by 9.5.2, 9.5.4, or 20.3.6, means the following:\n\t9.6.1. If "x" is the last agreed number fully uttered prior to the call, then the stall count resumes at “Stalling (x plus one)” or “Stalling n”, whichever of those two numbers is lower.\n‎‎‏‏‎ ‎')  



    if message.content.startswith('!10.'):

      if message.content.startswith('!10.1'):
        await message.channel.send('10.1. Whenever play stops during a point for a foul, violation, contested turnover, specified turnover, contested goal, stoppage, discussion, or at the completion of a time-out, play must restart as quickly as possible with a check. The check may only be delayed for the discussion of a call.')  

      elif message.content.startswith('!10.2'):
        await message.channel.send('10.2. Player positioning after a call (except in the case of a time-out, and unless specified otherwise):\n\t10.2.1. If play stops before a pass is thrown, all players must return to the location they held when the call was made.\n\t10.2.2. If play stops after a pass is thrown, then:\n\t\t10.2.2.1. if the disc is returned to the thrower, all players must return to the location they held when the thrower released the disc, or the time of the call, whichever is earlier.\n\t\t10.2.2.2. if the result of the play stands all players must return to the location they held when either a player established possession, or the disc hit the ground.\n\t\t10.2.2.3. if a player other than the thrower gains possession as a result of an accepted breach, all players must return to the location they held when the breach occurred.\n\t10.2.3. All players must remain stationary in that location until the disc is checked in.')  

      elif message.content.startswith('!10.3'):   
        await message.channel.send('10.3. Any player may briefly extend a stoppage of play to fix faulty equipment (“equipment”), but active play may not be stopped for this purpose.')  

      elif message.content.startswith('!10.4'): 
       await message.channel.send('10.4. Prior to the check the person checking the disc in, and the nearest opposition player, must verify that their own team-mates are ready, and positioned as per 10.2.')  

      elif message.content.startswith('!10.5'):    
        await message.channel.send('10.5. If there is an unnecessary delay in checking the disc in, the opposition may give a warning (“Delay of Game”). If the delay continues, the team that gave the warning may check the disc in by calling “Disc In”, without verification from the opposition, but only if the team checking the disc in are all stationary, and positioned as per 10.2. ')  

      elif message.content.startswith('!10.6'):   
        await message.channel.send('10.6. To restart play with a check: \n\t10.6.1. when the thrower has the disc:\n\t\t10.6.1.1. if there is a defender within reach, the defender must touch the disc.\n\t\t10.6.1.2. if there is not a defender within reach, the thrower must touch the disc to the ground and may call “Disc In”.\n\t10.6.2. when the disc is on the ground, the defender nearest to the disc must call “Disc In”.')  

      elif message.content.startswith('!10.7'):    
        await message.channel.send('10.7. A player may call a violation regarding the check if an opponent:\n\t10.7.1. attempts a pass without an appropriate check as per 10.6; or\n\t10.7.2. restarts play without verification from their nearest opposition player; or\n\t10.7.3. is moving immediately prior to the check; or\n\t10.7.4. was not in the appropriate position.\n\t10.7.5. After this violation call any pass does not count regardless of whether it is complete or incomplete, and possession reverts back to the thrower (unless 16.3 applies).') 

      else:
        await message.channel.send('10. The Check\n‎‎‏‏‎ ‎  ‎')        
        await message.channel.send('10.1. Whenever play stops during a point for a foul, violation, contested turnover, specified turnover, contested goal, stoppage, discussion, or at the completion of a time-out, play must restart as quickly as possible with a check. The check may only be delayed for the discussion of a call.\n‎‎‏‏‎ ‎ ') 
        await message.channel.send('10.2. Player positioning after a call (except in the case of a time-out, and unless specified otherwise):\n\t10.2.1. If play stops before a pass is thrown, all players must return to the location they held when the call was made.\n\t10.2.2. If play stops after a pass is thrown, then:\n\t\t10.2.2.1. if the disc is returned to the thrower, all players must return to the location they held when the thrower released the disc, or the time of the call, whichever is earlier.\n\t\t10.2.2.2. if the result of the play stands all players must return to the location they held when either a player established possession, or the disc hit the ground.\n\t\t10.2.2.3. if a player other than the thrower gains possession as a result of an accepted breach, all players must return to the location they held when the breach occurred.\n\t10.2.3. All players must remain stationary in that location until the disc is checked in.‎\n‎‎‏‏‎ ')  
        await message.channel.send('10.3. Any player may briefly extend a stoppage of play to fix faulty equipment (“equipment”), but active play may not be stopped for this purpose.\n‎‎‏‏‎ ‎')  
        await message.channel.send('10.4. Prior to the check the person checking the disc in, and the nearest opposition player, must verify that their own team-mates are ready, and positioned as per 10.2.\n‎‎‏‏‎ ‎')
        await message.channel.send('10.5. If there is an unnecessary delay in checking the disc in, the opposition may give a warning (“Delay of Game”). If the delay continues, the team that gave the warning may check the disc in by calling “Disc In”, without verification from the opposition, but only if the team checking the disc in are all stationary, and positioned as per 10.2. \n‎‎‏‏‎ ‎')  
        await message.channel.send('10.6. To restart play with a check: \n\t10.6.1. when the thrower has the disc:\n\t\t10.6.1.1. if there is a defender within reach, the defender must touch the disc.\n\t\t10.6.1.2. if there is not a defender within reach, the thrower must touch the disc to the ground and may call “Disc In”.\n\t10.6.2. when the disc is on the ground, the defender nearest to the disc must call “Disc In”.\n‎‎‏‏‎ ‎')  
        await message.channel.send('10.7. A player may call a violation regarding the check if an opponent:\n\t10.7.1. attempts a pass without an appropriate check as per 10.6; or\n\t10.7.2. restarts play without verification from their nearest opposition player; or\n\t10.7.3. is moving immediately prior to the check; or\n\t10.7.4. was not in the appropriate position.\n\t10.7.5. After this violation call any pass does not count regardless of whether it is complete or incomplete, and possession reverts back to the thrower (unless 16.3 applies).\n‎‎‏‏‎ ‎') 
      


    if message.content.startswith('!11.'):

      if message.content.startswith('!11.1'):
        await message.channel.send('11.1. The entire playing field is in-bounds. The perimeter lines are not part of the playing field and are out-of-bounds.  All non-players are part of the out-of-bounds area.')  

      elif message.content.startswith('!11.2'):
        await message.channel.send('11.2. The out-of-bounds area consists of the ground which is not in-bounds and everything in contact with it, except for defensive players, who are always considered “in-bounds”.')  

      elif message.content.startswith('!11.3'):   
        await message.channel.send('11.3. An offensive player who is not out-of-bounds is in-bounds.\n\t11.3.1. An airborne player retains their in-bounds/out-of-bounds status until that player contacts the playing field or the out-of-bounds area. \n\t11.3.2. A player who has caught the disc, who contacts the playing field and then contacts an out-of-bounds area, is still considered in-bounds, as long as they maintain the catch until they establish possession.\n\t\t11.3.2.1. If they leave the playing field, they must establish a pivot point at the location on the playing field where they crossed the perimeter line (unless 14.3 is in effect).\n\t11.3.3. A thrower who contacts an out-of-bounds area is considered in-bounds until they make a pass.\n\t11.3.4. Contact between players does not confer the state of being in- or out-of-bounds from one to another.')  

      elif message.content.startswith('!11.4'): 
       await message.channel.send('11.4. The following are out-of-bounds turnovers, and no catch is deemed to have occurred:\n\t11.4.1. any part of an offensive receiver is out-of-bounds when they contact the disc; or\n\t11.4.2. after catching the disc while airborne, an offensive receiver’s first contact is out-of-bounds while still in contact with the disc.')  

      elif message.content.startswith('!11.5'):    
        await message.channel.send('11.5. A disc is in-bounds once play is live, or when play starts or restarts.')  

      elif message.content.startswith('!11.6'):   
        await message.channel.send('11.6. A disc becomes out-of-bounds when it first contacts the out-of-bounds area or contacts an out-of-bounds offensive player.  A disc that has been caught by an offensive player has the same in/out-of-bounds status as that player.  If the disc is simultaneously caught by more than one offensive player, one of them being out-of-bounds, the disc is out-of-bounds.')  

      elif message.content.startswith('!11.7'):    
        await message.channel.send('11.7. The disc may fly outside a perimeter line and return to the playing field, and players may go out-of-bounds to make a play on the disc. ') 

      elif message.content.startswith('!11.8'):    
        await message.channel.send('11.8. The place where a disc went out-of-bounds is the location where, prior to contacting an out-of-bounds area or player, the disc was most recently: \n\t11.8.1. partly or wholly over the playing field; or\n\t11.8.2. contacted by an in-bounds player.') 

      elif message.content.startswith('!11.9'):    
        await message.channel.send('11.9. If the disc is out-of-bounds and more than three (3) metres from the pivot location, non-players may retrieve the disc.  The thrower must carry the disc the last three (3) metres to the playing field. ') 

      else:
        await message.channel.send('11. Out-of-Bounds\n‎‎‏‏‎ ‎  ‎')        
        await message.channel.send('11.1. The entire playing field is in-bounds. The perimeter lines are not part of the playing field and are out-of-bounds.  All non-players are part of the out-of-bounds area.\n‎‎‏‏‎ ‎ ') 
        await message.channel.send('11.2. The out-of-bounds area consists of the ground which is not in-bounds and everything in contact with it, except for defensive players, who are always considered “in-bounds”.‎\n‎‎‏‏‎ ')  
        await message.channel.send('11.3. An offensive player who is not out-of-bounds is in-bounds.\n\t11.3.1. An airborne player retains their in-bounds/out-of-bounds status until that player contacts the playing field or the out-of-bounds area. \n\t11.3.2. A player who has caught the disc, who contacts the playing field and then contacts an out-of-bounds area, is still considered in-bounds, as long as they maintain the catch until they establish possession.\n\t\t11.3.2.1. If they leave the playing field, they must establish a pivot point at the location on the playing field where they crossed the perimeter line (unless 14.3 is in effect).\n\t11.3.3. A thrower who contacts an out-of-bounds area is considered in-bounds until they make a pass.\n\t11.3.4. Contact between players does not confer the state of being in- or out-of-bounds from one to another.\n‎‎‏‏‎ ‎')  
        await message.channel.send('11.4. The following are out-of-bounds turnovers, and no catch is deemed to have occurred:\n\t11.4.1. any part of an offensive receiver is out-of-bounds when they contact the disc; or\n\t11.4.2. after catching the disc while airborne, an offensive receiver’s first contact is out-of-bounds while still in contact with the disc.\n‎‎‏‏‎ ‎')
        await message.channel.send('11.5. A disc is in-bounds once play is live, or when play starts or restarts.\n‎‎‏‏‎ ‎')  
        await message.channel.send('11.6. A disc becomes out-of-bounds when it first contacts the out-of-bounds area or contacts an out-of-bounds offensive player.  A disc that has been caught by an offensive player has the same in/out-of-bounds status as that player.  If the disc is simultaneously caught by more than one offensive player, one of them being out-of-bounds, the disc is out-of-bounds.\n‎‎‏‏‎ ‎')  
        await message.channel.send('11.7. The disc may fly outside a perimeter line and return to the playing field, and players may go out-of-bounds to make a play on the disc. \n‎‎‏‏‎ ‎') 
        await message.channel.send('11.8. The place where a disc went out-of-bounds is the location where, prior to contacting an out-of-bounds area or player, the disc was most recently: \n\t11.8.1. partly or wholly over the playing field; or\n\t11.8.2. contacted by an in-bounds player.\n‎‎‏‏‎ ‎')      
        await message.channel.send('11.9. If the disc is out-of-bounds and more than three (3) metres from the pivot location, non-players may retrieve the disc.  The thrower must carry the disc the last three (3) metres to the playing field.\n‎‎‏‏‎ ‎') 



    if message.content.startswith('!12.'):

        if message.content.startswith('!12.1'):


          if message.content.startswith('!12.10'):
            await message.channel.send('12.10. No player may physically assist the movement of another player, nor use an item of equipment or object to assist in contacting the disc.') 

          else:
            await message.channel.send('12.1. A “catch” occurs when a player has a non-spinning disc trapped between at least two body parts. A catch can enable a player to establish possession of the disc.\n\t12.1.1. If the player fails to maintain the catch due to subsequent ground contact related to the catch, or contact related to the catch with a team-mate or a legitimately positioned opposition player, possession is deemed to have not occurred.')  
        
        elif message.content.startswith('!12.2'):
          await message.channel.send('12.2. After establishing possession, that player becomes the thrower.')

        elif message.content.startswith('!12.3'):
          await message.channel.send('12.3. If offensive and defensive players catch the disc simultaneously, the offence retains possession.')

        elif message.content.startswith('!12.4'):
          await message.channel.send('12.4. A player in an established position is entitled to remain in that position and must not be contacted by an opposing player.')

        elif message.content.startswith('!12.5'):
          await message.channel.send('12.5. Every player is entitled to occupy any position on the field not occupied by any opposing player, provided that they do not initiate contact in taking such a position, and are not moving in a reckless or dangerously aggressive manner. \n\t12.5.1. However when the disc is in the air a player may not move in a manner solely to prevent an opponent from taking an unoccupied path to make a play on the disc.')

        elif message.content.startswith('!12.6'):
         await message.channel.send('12.6. All players must attempt to avoid contact with other players, and there is no situation where a player may justify initiating contact. This includes avoiding initiating contact with a stationary opponent, or an opponent’s expected position based on their established speed and direction.  “Making a play for the disc” is not a valid excuse for initiating contact with other players. \n\t12.6.1. If a player is not reasonably certain that they will be able to make a legal play at the disc before an opponent who is moving in a legal manner, they must adjust their movements to avoid initiating contact. If that adjustment is made, the result of the play still stands.')     

        elif message.content.startswith('!12.7'):
         await message.channel.send('12.7.The player who initiates contact is deemed to be the player who:\n\t12.7.1. arrived at the point of contact after the opponent had already established a legitimate position at that point (either a stationary or moving opponent), or\n\t12.7.2. adjusted their movements in a way that created unavoidable contact with an opponent moving in a legal manner, when taking into account all players’ established position, speed and direction.')    
        elif message.content.startswith('!12.8'):
          await message.channel.send('12.8. Some minor contact may occur as two or more players move towards a single point simultaneously. Minor contact should be minimized but is not considered a foul. ') 

        elif message.content.startswith('!12.9'):
          await message.channel.send('12.9. Players may not use their arms or legs to obstruct the movement of opposing players.')        
        else:
          await message.channel.send('12. Receivers and Positioning\n‎‎‏‏‎ ‎')
          await message.channel.send('12.1. A “catch” occurs when a player has a non-spinning disc trapped between at least two body parts. A catch can enable a player to establish possession of the disc.\n\t12.1.1. If the player fails to maintain the catch due to subsequent ground contact related to the catch, or contact related to the catch with a team-mate or a legitimately positioned opposition player, possession is deemed to have not occurred.\n‎‎‏‏‎ ‎')

          await message.channel.send('12.2. After establishing possession, that player becomes the thrower.\n‎‎‏‏‎ ')

          await message.channel.send('12.3. If offensive and defensive players catch the disc simultaneously, the offence retains possession.\n‎‎‏‏‎ ')

          await message.channel.send('12.4. A player in an established position is entitled to remain in that position and must not be contacted by an opposing player.\n‎‎‏‏‎ ')  

          await message.channel.send('12.5. Every player is entitled to occupy any position on the field not occupied by any opposing player, provided that they do not initiate contact in taking such a position, and are not moving in a reckless or dangerously aggressive manner. \n\t12.5.1. However when the disc is in the air a player may not move in a manner solely to prevent an opponent from taking an unoccupied path to make a play on the disc.\n‎‎‏‏‎ ')

          await message.channel.send('12.6. All players must attempt to avoid contact with other players, and there is no situation where a player may justify initiating contact. This includes avoiding initiating contact with a stationary opponent, or an opponent’s expected position based on their established speed and direction.  “Making a play for the disc” is not a valid excuse for initiating contact with other players. \n\t12.6.1. If a player is not reasonably certain that they will be able to make a legal play at the disc before an opponent who is moving in a legal manner, they must adjust their movements to avoid initiating contact. If that adjustment is made, the result of the play still stands.\n‎‎‏‏‎ ') 

          await message.channel.send('12.7.The player who initiates contact is deemed to be the player who:\n\t12.7.1. arrived at the point of contact after the opponent had already established a legitimate position at that point (either a stationary or moving opponent), or\n\t12.7.2. adjusted their movements in a way that created unavoidable contact with an opponent moving in a legal manner, when taking into account all players’ established position, speed and direction.\n‎‎‏‏‎ ') 

          await message.channel.send('12.8. Some minor contact may occur as two or more players move towards a single point simultaneously. Minor contact should be minimized but is not considered a foul.\n‎‎‏‏‎ ')

          await message.channel.send('12.9. Players may not use their arms or legs to obstruct the movement of opposing players.\n‎‎‏‏‎ ')

          await message.channel.send('12.10. No player may physically assist the movement of another player, nor use an item of equipment or object to assist in contacting the disc.\n‎‎‏‏‎ ') 



    if message.content.startswith('!13.'):

        if message.content.startswith('!13.1'):


          if message.content.startswith('!13.10'):
            await message.channel.send('13.10. If the turnover location is in the offence’s attacking end zone, the thrower must establish a pivot point at the nearest location on the goal line.') 

          elif message.content.startswith('!13.11'):
            await message.channel.send('13.11. If the turnover location is in the offence’s defending end zone, the thrower may choose where to establish a pivot point:\n\t13.11.1. at the turnover location, by staying at the turnover location or faking a pass; or\n\t13.11.2. at the nearest location on the goal line to the turnover location, by moving from the turnover location.\n\t\t13.11.2.1. The intended thrower, before picking up the disc, may signal the goal line option by fully extending one arm above their head. \n\t13.11.3. Immediate movement, staying at the turnover location, faking a pass, or signaling the goal line option determines where to establish a pivot point and cannot be reversed. ') 

          elif message.content.startswith('!13.12'):
            await message.channel.send('13.12. If, after an accepted turnover, play has continued unknowingly, play stops and the disc is returned to the turnover location, players resume their positions at the time the turnover occurred and play restarts with a check.') 

          else:
            await message.channel.send('13.1. A turnover that transfers possession of the disc from one team to the other occurs when:\n\t13.1.1. the disc contacts the ground while it is not in the possession of an offensive player (a “down”); \n\t\t13.1.1.1. however it is not “down” if a receiver catches a pass before the disc contacts the ground, and maintains the catch while the disc is in contact with the ground.\n\t13.1.2. a defensive player establishes possession of a pass (an “interception”);\n\t13.1.3. the disc becomes out-of-bounds (an “out-of-bounds” or "out"); or\n\t13.1.4. during the pull, the offence touches the disc before it hits the ground, and subsequently fails to establish possession of the disc (a “dropped pull”).')  
        
        elif message.content.startswith('!13.2'):
          await message.channel.send('13.2. A turnover that transfers possession of the disc from one team to the other, and results in a stoppage of play, occurs when:\n\t13.2.1. there is an accepted offensive receiving foul;\n\t13.2.2. the thrower has not released the disc before the marker first starts to say the word “ten” in the stall count (a “stall-out”);\\t13.2.3. the disc is intentionally transferred from one offensive player to another without ever being completely untouched by both players (a “hand-over”);\n\t13.2.4. the thrower intentionally deflects a pass to themselves off another player (a “deflection”);\n\t13.2.5. in attempting a pass, the thrower catches the disc after release prior to the disc being contacted by another player (a “self-catch”); \n\t13.2.6. an offensive player intentionally assists a team-mate’s movement to catch a pass; or\n\t13.2.7. an offensive player uses an item of equipment or object to assist in catching a pass.')

        elif message.content.startswith('!13.3'):
          await message.channel.send('13.3. If a player determines a turnover has occurred they must make the appropriate call immediately.  If the opposition disagrees they may call "contest" and play must stop. If, after discussion, players cannot agree or it is unclear what occurred in the play, the disc must be returned to the last non-disputed thrower.')

        elif message.content.startswith('!13.4'):
          await message.channel.send('13.4. After a “stall-out” call:\n\t13.4.1. If the thrower still has possession of the disc, but they believe a fast count occurred in such a manner that they did not have a reasonable opportunity to call fast count before a stall-out, the play is treated as either an accepted defensive breach (9.5.1) or a contested stall-out (9.5.3).\n\t13.4.2. If the thrower made a completed pass, the thrower can contest if they believe it was not a “stall-out”, or there was a fast count immediately prior to the “stall-out”.\n\t13.4.3. If the thrower contests a stall-out but also attempts a pass, and the pass is incomplete, then the turnover stands and play restarts with a check.')

        elif message.content.startswith('!13.5'):
          await message.channel.send('13.5. Any offensive player may take possession of the disc after a turnover, except:\n\t13.5.1. after an “interception” turnover, in which case the player who made the interception must maintain possession; and \n\t13.5.2. after an offensive receiving foul, in which case the fouled player must take possession.')

        elif message.content.startswith('!13.6'):
         await message.channel.send('13.6. If the player in possession after a turnover, or after a pull that has already hit the ground, intentionally drops the disc, places the disc on the ground, or transfers possession of the disc, they must re-establish possession and restart play with a check.')     

        elif message.content.startswith('!13.7'):
         await message.channel.send('13.7. After a turnover, the turnover location is where:\n\t13.7.1. the disc has come to a stop or is picked up by an offensive player; or\n\t13.7.2. the intercepting player stops; or\n\t13.7.3. the thrower was located at the time of the call, in the case of 13.2.2, 13.2.3, 13.2.4, 13.2.5; or\n\t13.7.4. the offensive player was located, in the case of 13.2.6 and 13.2.7; or\n\t13.7.5. the accepted offensive receiving foul occurred.')    

        elif message.content.startswith('!13.8'):
          await message.channel.send('13.8. If the turnover location is out-of-bounds, or the disc touched an out-of-bounds area after the turnover occurred, the thrower must establish a pivot point at the location on the central zone nearest to where the disc went out-of-bounds (Section 11.8). \n\t13.8.1. If 13.8 does not apply, a pivot point must be established according to 13.9, 13.10, or 13.11.') 

        elif message.content.startswith('!13.9'):
          await message.channel.send('13.9. If the turnover location is in the central zone, the thrower must establish a pivot point at that location.')        

        else:
          await message.channel.send('13. Turnovers\n‎‎‏‏‎ ‎')
          await message.channel.send('13.1. A turnover that transfers possession of the disc from one team to the other occurs when:\n\t13.1.1. the disc contacts the ground while it is not in the possession of an offensive player (a “down”); \n\t\t13.1.1.1. however it is not “down” if a receiver catches a pass before the disc contacts the ground, and maintains the catch while the disc is in contact with the ground.\n\t13.1.2. a defensive player establishes possession of a pass (an “interception”);\n\t13.1.3. the disc becomes out-of-bounds (an “out-of-bounds” or "out"); or\n\t13.1.4. during the pull, the offence touches the disc before it hits the ground, and subsequently fails to establish possession of the disc (a “dropped pull”).\n‎‎‏‏‎ ‎')

          await message.channel.send('13.2. A turnover that transfers possession of the disc from one team to the other, and results in a stoppage of play, occurs when:\n\t13.2.1. there is an accepted offensive receiving foul;\n\t13.2.2. the thrower has not released the disc before the marker first starts to say the word “ten” in the stall count (a “stall-out”);\\t13.2.3. the disc is intentionally transferred from one offensive player to another without ever being completely untouched by both players (a “hand-over”);\n\t13.2.4. the thrower intentionally deflects a pass to themselves off another player (a “deflection”);\n\t13.2.5. in attempting a pass, the thrower catches the disc after release prior to the disc being contacted by another player (a “self-catch”); \n\t13.2.6. an offensive player intentionally assists a team-mate’s movement to catch a pass; or\n\t13.2.7. an offensive player uses an item of equipment or object to assist in catching a pass.\n‎‎‏‏‎ ')

          await message.channel.send('13.3. If a player determines a turnover has occurred they must make the appropriate call immediately.  If the opposition disagrees they may call "contest" and play must stop. If, after discussion, players cannot agree or it is unclear what occurred in the play, the disc must be returned to the last non-disputed thrower.\n‎‎‏‏‎ ')

          await message.channel.send('13.4. After a “stall-out” call:\n\t13.4.1. If the thrower still has possession of the disc, but they believe a fast count occurred in such a manner that they did not have a reasonable opportunity to call fast count before a stall-out, the play is treated as either an accepted defensive breach (9.5.1) or a contested stall-out (9.5.3).\n\t13.4.2. If the thrower made a completed pass, the thrower can contest if they believe it was not a “stall-out”, or there was a fast count immediately prior to the “stall-out”.\n\t13.4.3. If the thrower contests a stall-out but also attempts a pass, and the pass is incomplete, then the turnover stands and play restarts with a check.\n‎‎‏‏‎ ')  

          await message.channel.send('13.5. Any offensive player may take possession of the disc after a turnover, except:\n\t13.5.1. after an “interception” turnover, in which case the player who made the interception must maintain possession; and \n\t13.5.2. after an offensive receiving foul, in which case the fouled player must take possession.\n‎‎‏‏‎ ')

          await message.channel.send('13.6. If the player in possession after a turnover, or after a pull that has already hit the ground, intentionally drops the disc, places the disc on the ground, or transfers possession of the disc, they must re-establish possession and restart play with a check.\n‎‎‏‏‎ ') 

          await message.channel.send('13.7. After a turnover, the turnover location is where:\n\t13.7.1. the disc has come to a stop or is picked up by an offensive player; or\n\t13.7.2. the intercepting player stops; or\n\t13.7.3. the thrower was located at the time of the call, in the case of 13.2.2, 13.2.3, 13.2.4, 13.2.5; or\n\t13.7.4. the offensive player was located, in the case of 13.2.6 and 13.2.7; or\n\t13.7.5. the accepted offensive receiving foul occurred.\n‎‎‏‏‎ ') 

          await message.channel.send('13.8. If the turnover location is out-of-bounds, or the disc touched an out-of-bounds area after the turnover occurred, the thrower must establish a pivot point at the location on the central zone nearest to where the disc went out-of-bounds (Section 11.8). \n\t13.8.1. If 13.8 does not apply, a pivot point must be established according to 13.9, 13.10, or 13.11.\n‎‎‏‏‎ ')

          await message.channel.send('13.9. If the turnover location is in the central zone, the thrower must establish a pivot point at that location.\n‎‎‏‏‎ ')

          await message.channel.send('13.10. If the turnover location is in the offence’s attacking end zone, the thrower must establish a pivot point at the nearest location on the goal line.\n‎‎‏‏‎ ') 

          await message.channel.send('13.11. If the turnover location is in the offence’s defending end zone, the thrower may choose where to establish a pivot point:\n\t13.11.1. at the turnover location, by staying at the turnover location or faking a pass; or\n\t13.11.2. at the nearest location on the goal line to the turnover location, by moving from the turnover location.\n\t\t13.11.2.1. The intended thrower, before picking up the disc, may signal the goal line option by fully extending one arm above their head. \n\t13.11.3. Immediate movement, staying at the turnover location, faking a pass, or signaling the goal line option determines where to establish a pivot point and cannot be reversed.\n‎‎‏‏‎ ') 

          await message.channel.send('13.12. If, after an accepted turnover, play has continued unknowingly, play stops and the disc is returned to the turnover location, players resume their positions at the time the turnover occurred and play restarts with a check.\n‎‎‏‏‎ ')  
   


    if message.content.startswith('!14.'):

      if message.content.startswith('!14.1'):
        await message.channel.send('14.1. A goal is scored if an in-bounds player catches a legal pass and:\n\t14.1.1. all their ground contacts are entirely within their attacking end zone, or for an airborne player, all of their first simultaneous points of ground contact after catching the disc are entirely within their attacking end zone, and \n\t14.1.2. they subsequently establish possession of the disc, and maintain the catch throughout all ground contact related to the catch (note 12.1, 12.1.1). ')  

      elif message.content.startswith('!14.2'):
        await message.channel.send('14.2. If a player believes a goal has been scored, they may call “goal” and play stops. After a contested or retracted goal call play must restart with a check and the call is deemed to have been made when the player established possession.')  

      elif message.content.startswith('!14.3'):
        await message.channel.send('14.3. If a player in possession of the disc ends up with their selected pivot point behind the attacking goal line without scoring a goal according to 14.1, the player must establish a pivot point at the nearest location on the goal line.')  

      elif message.content.startswith('!14.4'):
        await message.channel.send('14.4. The time at which a goal is deemed to have been scored is when the player established possession.')  
      
      else:
        await message.channel.send('14. Scoring\n‎‎‏‏‎ ‎  ‎')
        await message.channel.send('14.1. A goal is scored if an in-bounds player catches a legal pass and:\n\t14.1.1. all their ground contacts are entirely within their attacking end zone, or for an airborne player, all of their first simultaneous points of ground contact after catching the disc are entirely within their attacking end zone, and \n\t14.1.2. they subsequently establish possession of the disc, and maintain the catch throughout all ground contact related to the catch (note 12.1, 12.1.1).\n‎‎‏‏‎ ‎ ')  
        await message.channel.send('14.2. If a player believes a goal has been scored, they may call “goal” and play stops. After a contested or retracted goal call play must restart with a check and the call is deemed to have been made when the player established possession.\n‎‎‏‏‎ ‎')  
        await message.channel.send('14.3. If a player in possession of the disc ends up with their selected pivot point behind the attacking goal line without scoring a goal according to 14.1, the player must establish a pivot point at the nearest location on the goal line.\n‎‎‏‏‎ ‎ ')
        await message.channel.send('14.4. The time at which a goal is deemed to have been scored is when the player established possession.\n‎‎‏‏‎ ‎ ') 



    if message.content.startswith('!15.'):

        if message.content.startswith('!15.1'):


          if message.content.startswith('!15.10'):
            await message.channel.send('15.10. If the player against whom the foul, infraction or violation has been called disagrees that it occurred, or does not think it is a correct call, they may call “Contest”.') 

          elif message.content.startswith('!15.11'):
            await message.channel.send('15.11. If a player making any call subsequently determines that their call was incorrect, they can retract the call, by calling "Retracted". The stall count resumes as if an accepted breach has been caused by that player.') 

          elif message.content.startswith('!15.12'):
            await message.channel.send('15.12. If multiple breaches occur on the same play or before play stops, the outcomes should be resolved in reverse sequence (latest breach first, earliest breach last).') 

          elif message.content.startswith('!15.13'):
            await message.channel.send('15.13. Players are encouraged to use the WFDF Hand Signals to communicate all calls.') 

          else:
            await message.channel.send('15.1. A breach of the rules due to non-minor contact between two or more opposing players is a foul. \n\t15.1.1. A player intentionally initiating minor contact is still a breach of the rules, but is to be treated as a violation, and not a foul.')  
        elif message.content.startswith('!15.2'):
          await message.channel.send('15.2. A breach of the rules regarding a Marking or Travel breach is an infraction.  Infractions do not stop play.')

        elif message.content.startswith('!15.3'):
          await message.channel.send('15.3. Every other breach of the rules is a violation.')

        elif message.content.startswith('!15.4'):
          await message.channel.send('15.4. Only the player fouled may claim a foul, by calling “Foul”.')

        elif message.content.startswith('!15.5'):
          await message.channel.send('15.5. In general only the thrower may claim an infraction, by calling the specific name of the infraction.\n\t15.5.1. However any offensive player may call a double team, and any defensive player may call a travel infraction.')

        elif message.content.startswith('!15.6'):
         await message.channel.send('15.6. Any opposing player may claim a violation, by calling the specific name of the violation or "Violation", unless specified otherwise by the particular rule.')     

        elif message.content.startswith('!15.7'):
         await message.channel.send('15.7. When a foul or violation call is made that stops play, players must stop play by visibly or audibly communicating the stoppage as soon as they are aware of the call and all players should echo calls on the field. If play has stopped for a discussion without any call having been made, a call is deemed to have been made when the discussion started.')    

        elif message.content.startswith('!15.8'):
          await message.channel.send('15.8. Calls must be made immediately after the breach is recognised.') 

        elif message.content.startswith('!15.9'):
          await message.channel.send('15.9. After a player initiates a stoppage incorrectly, including after mishearing a call, not knowing the rules, or not making the call immediately:\n\t15.9.1. if the opposition gains or retains possession, any subsequent play stands.\n\t15.9.2. if the opposition does not gain or retain possession, the disc must be returned to the last non-disputed thrower, unless 16.3 applies. The stall count resumes as if an accepted breach has been caused by the player who initiated the stoppage incorrectly.')        

        else:
          await message.channel.send('15. Calling Fouls, Infractions and Violations\n‎‎‏‏‎ ‎')
          await message.channel.send('15.1. A breach of the rules due to non-minor contact between two or more opposing players is a foul. \n\t15.1.1. A player intentionally initiating minor contact is still a breach of the rules, but is to be treated as a violation, and not a foul.\n‎‎‏‏‎ ‎')

          await message.channel.send('15.2. A breach of the rules regarding a Marking or Travel breach is an infraction.  Infractions do not stop play.\n‎‎‏‏‎ ')

          await message.channel.send('15.3. Every other breach of the rules is a violation.\n‎‎‏‏‎ ')

          await message.channel.send('15.4. Only the player fouled may claim a foul, by calling “Foul”.\n‎‎‏‏‎ ')  

          await message.channel.send('15.5. In general only the thrower may claim an infraction, by calling the specific name of the infraction.\n\t15.5.1. However any offensive player may call a double team, and any defensive player may call a travel infraction.\n‎‎‏‏‎ ')

          await message.channel.send('15.6. Any opposing player may claim a violation, by calling the specific name of the violation or "Violation", unless specified otherwise by the particular rule.\n‎‎‏‏‎ ') 

          await message.channel.send('15.7. When a foul or violation call is made that stops play, players must stop play by visibly or audibly communicating the stoppage as soon as they are aware of the call and all players should echo calls on the field. If play has stopped for a discussion without any call having been made, a call is deemed to have been made when the discussion started.\n‎‎‏‏‎ ') 

          await message.channel.send('15.8. Calls must be made immediately after the breach is recognised.\n‎‎‏‏‎ ')

          await message.channel.send('15.9. After a player initiates a stoppage incorrectly, including after mishearing a call, not knowing the rules, or not making the call immediately:\n\t15.9.1. if the opposition gains or retains possession, any subsequent play stands.\n\t15.9.2. if the opposition does not gain or retain possession, the disc must be returned to the last non-disputed thrower, unless 16.3 applies. The stall count resumes as if an accepted breach has been caused by the player who initiated the stoppage incorrectly.\n‎‎‏‏‎ ')

          await message.channel.send('15.10. If the player against whom the foul, infraction or violation has been called disagrees that it occurred, or does not think it is a correct call, they may call “Contest”.\n‎‎‏‏‎ ') 

          await message.channel.send('15.11. If a player making any call subsequently determines that their call was incorrect, they can retract the call, by calling "Retracted". The stall count resumes as if an accepted breach has been caused by that player.\n‎‎‏‏‎ ') 

          await message.channel.send('15.12. If multiple breaches occur on the same play or before play stops, the outcomes should be resolved in reverse sequence (latest breach first, earliest breach last).\n‎‎‏‏‎ ')  

          await message.channel.send('15.13. Players are encouraged to use the WFDF Hand Signals to communicate all calls.\n‎‎‏‏‎ ')     
  


    if message.content.startswith('!16.'):

      if message.content.startswith('!16.1'):
        await message.channel.send('16.1. Whenever a foul or violation call is made, or a player attempts to stop play in any way, play stops immediately and no turn over is possible (unless in situations specified in 15.9, 16.2, and 16.3).')  

      elif message.content.startswith('!16.2'):
        await message.channel.send('16.2. If a foul or violation:\n\t16.2.1. is called against the thrower and the thrower attempts a pass, or\n\t16.2.2. is called by the thrower during the act of throwing, or\n\t16.2.3. is called or occurs when the disc is in the air, then play continues until possession has been established.\n\t16.2.4. Once possession has been established:\n\t\t16.2.4.1. If the team that called the foul or violation gains or retains possession as a result of the pass, the play stands. Play can continue without a stoppage if the player who made the foul or violation call makes a “Play on” call as soon as possible. \n\t\t16.2.4.2. If the team that called the foul or violation does not gain or retain possession as a result of the pass, play must be stopped.\n\t\t\t16.2.4.2.1. If the team that called the foul or violation believes that possession has been affected by the foul or violation, the disc will be returned to the thrower for a check (unless the specific rule says otherwise).')

      elif message.content.startswith('!16.3'):
        await message.channel.send('16.3. Regardless of when any call is made, if the players involved from both teams agree that the event or call did not affect the outcome, the play stands. This rule is not superseded by any other rule.\n\t16.3.1. If the play resulted in a goal, the goal stands.\n\t16.3.2. If the play did not result in a goal the affected players may make up any positional disadvantage caused by the event or call and restart play with a check.')  
      else:
        await message.channel.send('16. Continuation after a Call\n‎‎‏‏‎ ‎  ‎')
        await message.channel.send('16.1. Whenever a foul or violation call is made, or a player attempts to stop play in any way, play stops immediately and no turn over is possible (unless in situations specified in 15.9, 16.2, and 16.3).\n‎‎‏‏‎ ‎ ')  
        await message.channel.send('16.2. If a foul or violation:\n\t16.2.1. is called against the thrower and the thrower attempts a pass, or\n\t16.2.2. is called by the thrower during the act of throwing, or\n\t16.2.3. is called or occurs when the disc is in the air, then play continues until possession has been established.\n\t16.2.4. Once possession has been established:\n\t\t16.2.4.1. If the team that called the foul or violation gains or retains possession as a result of the pass, the play stands. Play can continue without a stoppage if the player who made the foul or violation call makes a “Play on” call as soon as possible. \n\t\t16.2.4.2. If the team that called the foul or violation does not gain or retain possession as a result of the pass, play must be stopped.\n\t\t\t16.2.4.2.1. If the team that called the foul or violation believes that possession has been affected by the foul or violation, the disc will be returned to the thrower for a check (unless the specific rule says otherwise).\n‎‎‏‏‎ ‎')  
        await message.channel.send('16.3. Regardless of when any call is made, if the players involved from both teams agree that the event or call did not affect the outcome, the play stands. This rule is not superseded by any other rule.\n\t16.3.1. If the play resulted in a goal, the goal stands.\n\t16.3.2. If the play did not result in a goal the affected players may make up any positional disadvantage caused by the event or call and restart play with a check.\n‎‎‏‏‎ ‎ ')
      


    if message.content.startswith('!17.'):

      if message.content.startswith('!17.1'):
        await message.channel.send('17.1. Dangerous Play:\n\n\t17.1.1. Actions demonstrating reckless disregard for the safety of fellow players, or posing significant risk of injury to fellow players, or other dangerously aggressive behaviours, are considered dangerous play and must be treated as a foul, regardless of whether or when contact occurs. This rule is not superseded by any other foul rule. If the dangerous play call is accepted, this must be treated as the most relevant foul from Section 17.')  

      elif message.content.startswith('!17.2'):
        await message.channel.send('17.2. Receiving Fouls:\n\n\t17.2.1. A Receiving Foul occurs when a player initiates non-minor contact with an opponent before, while, or directly after, either player makes a play on the disc. \n\t\t17.2.1.1. Contact with an opponent’s arms or hands, that occurs after the disc has been caught, or after the opponent can no longer make a play on the disc, is not a sufficient basis for a foul, but should be avoided (excluding contact related to Section 17.1 and 17.3).\n\n\t17.2.2. After an accepted receiving foul the fouled player gains possession at the location of the breach, even if that location is in an end zone, and play restarts with a check. If, after the check, 14.3 applies, the stall count can not be started until a pivot point is established at the nearest location on the goal line. If the foul is contested, the disc is returned to the thrower.')  

      elif message.content.startswith('!17.3'):   
        await message.channel.send('17.3. Strip Fouls:\n\n\t17.3.1. A Strip Foul occurs when an opponent fouls a player and that causes the player to drop a disc they caught or to lose possession of the disc.\n\n\t17.3.2. If the reception would have otherwise been a goal, and the foul is uncontested, a goal is awarded.')  

      elif message.content.startswith('!17.4'): 
       await message.channel.send('17.4. Blocking Fouls:\n\n\t17.4.1. A Blocking Foul occurs when a player takes a position that an opponent moving in a legal manner will be unable to avoid, taking into account the opponents expected position based on their established speed and direction, and non-minor contact results. This is to be treated as either a receiving foul or an indirect foul, whichever is applicable.')  

      elif message.content.startswith('!17.5'):    
        await message.channel.send('17.5. Force-out Fouls:\n\n\t17.5.1. A Force-out Foul occurs when a receiver is in the process of establishing possession of the disc, and is fouled by a defensive player before establishing possession, and the contact caused the receiver:\n\t\t17.5.1.1. to become out-of-bounds instead of in-bounds; or\n\t\t17.5.1.2. to catch the disc in the central zone instead of their attacking end zone.\n\n\t17.5.2. If the receiver would have caught the disc in their attacking end zone, it is a goal;\n\n\t17.5.3. If the force-out foul is contested, the disc is returned to the thrower if the receiver became out-of-bounds, otherwise the disc stays with the receiver.')  

      elif message.content.startswith('!17.6'):   
        await message.channel.send('17.6. Defensive Throwing (Marking) Fouls: \n\n\t17.6.1. A Defensive Throwing Foul occurs when:\n\t\t17.6.1.1. A defensive player is illegally positioned (Section 18.1), and there is non-minor contact between the illegally positioned defensive player and the thrower; or\n\t\t17.6.1.2. A defensive player initiates non-minor contact with the thrower, or there is non-minor contact resulting from the thrower and the defender both vying for the same unoccupied position, prior to the release.\n\t\t17.6.1.3. If a Defensive Throwing Foul occurs prior to the thrower releasing the disc and not during the throwing motion, the thrower may choose to call a contact infraction, by calling “Contact”. After a contact infraction that is not contested, play does not stop and the marker must resume the stall count at one (1).')  

      elif message.content.startswith('!17.7'):    
        await message.channel.send('17.7. Offensive Throwing (Thrower) Fouls:\n\n\t17.7.1. An Offensive Throwing Foul occurs when the thrower is solely responsible for initiating non-minor contact with a defensive player who is in a legal position. \n\n\t17.7.2. Contact occurring during the thrower\'s follow through is not a sufficient basis for a foul, but should be avoided.') 

      elif message.content.startswith('!17.8'):    
        await message.channel.send('17.8. Indirect Fouls:\n\n\t17.8.1. An Indirect Foul occurs when there is non-minor contact between a receiver and a defensive player that does not directly affect an attempt to make a play on the disc. \n\n\t17.8.2. If the foul is accepted the fouled player may make up any positional disadvantage caused by the foul.') 

      elif message.content.startswith('!17.9'):    
        await message.channel.send('17.9. Offsetting Fouls:\n\n\t17.9.1. If accepted fouls are called by offensive and defensive players on the same play, these are offsetting fouls, and the disc must be returned to the last non-disputed thrower.\n\n\t17.9.2. If there is non-minor contact that is caused by two or more opposing players moving towards a single point simultaneously, this must be treated as offsetting fouls. \n\t\t17.9.2.1. However if this occurs after the disc has been caught, or after the relevant player/s involved can no longer make a play on the disc, this must be treated as an Indirect Foul (excluding contact related to Section 17.1).') 

      else:
        await message.channel.send('17. Fouls\n‎‎‏‏‎ ‎  ‎')        
        await message.channel.send('17.1. Dangerous Play:\n\n\t17.1.1. Actions demonstrating reckless disregard for the safety of fellow players, or posing significant risk of injury to fellow players, or other dangerously aggressive behaviours, are considered dangerous play and must be treated as a foul, regardless of whether or when contact occurs. This rule is not superseded by any other foul rule. If the dangerous play call is accepted, this must be treated as the most relevant foul from Section 17.\n‎‎‏‏‎ ‎ ') 
        await message.channel.send('17.2. Receiving Fouls:\n\n\t17.2.1. A Receiving Foul occurs when a player initiates non-minor contact with an opponent before, while, or directly after, either player makes a play on the disc. \n\t\t17.2.1.1. Contact with an opponent’s arms or hands, that occurs after the disc has been caught, or after the opponent can no longer make a play on the disc, is not a sufficient basis for a foul, but should be avoided (excluding contact related to Section 17.1 and 17.3).\n\n\t17.2.2. After an accepted receiving foul the fouled player gains possession at the location of the breach, even if that location is in an end zone, and play restarts with a check. If, after the check, 14.3 applies, the stall count can not be started until a pivot point is established at the nearest location on the goal line. If the foul is contested, the disc is returned to the thrower.‎\n‎‎‏‏‎ ')  
        await message.channel.send('17.3. Strip Fouls:\n\n\t17.3.1. A Strip Foul occurs when an opponent fouls a player and that causes the player to drop a disc they caught or to lose possession of the disc.\n\n\t17.3.2. If the reception would have otherwise been a goal, and the foul is uncontested, a goal is awarded.\n‎‎‏‏‎ ‎')  
        await message.channel.send('17.4. Blocking Fouls:\n\n\t17.4.1. A Blocking Foul occurs when a player takes a position that an opponent moving in a legal manner will be unable to avoid, taking into account the opponents expected position based on their established speed and direction, and non-minor contact results. This is to be treated as either a receiving foul or an indirect foul, whichever is applicable.\n‎‎‏‏‎ ‎')
        await message.channel.send('17.5. Force-out Fouls:\n\n\t17.5.1. A Force-out Foul occurs when a receiver is in the process of establishing possession of the disc, and is fouled by a defensive player before establishing possession, and the contact caused the receiver:\n\t\t17.5.1.1. to become out-of-bounds instead of in-bounds; or\n\t\t17.5.1.2. to catch the disc in the central zone instead of their attacking end zone.\n\n\t17.5.2. If the receiver would have caught the disc in their attacking end zone, it is a goal;\n\n\t17.5.3. If the force-out foul is contested, the disc is returned to the thrower if the receiver became out-of-bounds, otherwise the disc stays with the receiver.\n‎‎‏‏‎ ‎')  
        await message.channel.send('17.6. Defensive Throwing (Marking) Fouls: \n\n\t17.6.1. A Defensive Throwing Foul occurs when:\n\t\t17.6.1.1. A defensive player is illegally positioned (Section 18.1), and there is non-minor contact between the illegally positioned defensive player and the thrower; or\n\t\t17.6.1.2. A defensive player initiates non-minor contact with the thrower, or there is non-minor contact resulting from the thrower and the defender both vying for the same unoccupied position, prior to the release.\n\t\t17.6.1.3. If a Defensive Throwing Foul occurs prior to the thrower releasing the disc and not during the throwing motion, the thrower may choose to call a contact infraction, by calling “Contact”. After a contact infraction that is not contested, play does not stop and the marker must resume the stall count at one (1).\n‎‎‏‏‎ ‎')  
        await message.channel.send('17.7. Offensive Throwing (Thrower) Fouls:\n\n\t17.7.1. An Offensive Throwing Foul occurs when the thrower is solely responsible for initiating non-minor contact with a defensive player who is in a legal position. \n\n\t17.7.2. Contact occurring during the thrower\'s follow through is not a sufficient basis for a foul, but should be avoided.\n‎‎‏‏‎ ‎') 
        await message.channel.send('17.8. Indirect Fouls:\n\n\t17.8.1. An Indirect Foul occurs when there is non-minor contact between a receiver and a defensive player that does not directly affect an attempt to make a play on the disc. \n\n\t17.8.2. If the foul is accepted the fouled player may make up any positional disadvantage caused by the foul.\n‎‎‏‏‎ ‎')      
        await message.channel.send('17.9. Offsetting Fouls:\n\n\t17.9.1. If accepted fouls are called by offensive and defensive players on the same play, these are offsetting fouls, and the disc must be returned to the last non-disputed thrower.\n\n\t17.9.2. If there is non-minor contact that is caused by two or more opposing players moving towards a single point simultaneously, this must be treated as offsetting fouls. \n\t\t17.9.2.1. However if this occurs after the disc has been caught, or after the relevant player/s involved can no longer make a play on the disc, this must be treated as an Indirect Foul (excluding contact related to Section 17.1).\n‎‎‏‏‎ ‎') 



    if message.content.startswith('!18.'):

      if message.content.startswith('!18.1'):
        await message.channel.send('18.1. Marking Infractions:\n\n\t18.1.1. Marking infractions include the following:\n\n\t\t18.1.1.1. “Fast Count” – the marker:\n\t\t\t18.1.1.1.1. starts or continues the stall count illegally,\n\t\t\t18.1.1.1.2. does not start or restart the stall count with the word “Stalling”,\n\t\t\t18.1.1.1.3. counts in less than one second intervals,\n\t\t\t18.1.1.1.4. does not correctly reduce or reset the stall count when required, or\n\t\t\t18.1.1.1.5. does not start the stall count from the correct number.\n\n\t\t18.1.1.2. “Straddle” – a line between a defensive player’s feet comes within one disc diameter of the thrower’s pivot point.\n\n\t\t18.1.1.3. “Disc Space” – any part of a defensive player is less than one disc diameter away from the torso of the thrower.  However, if this situation is caused solely by movement of the thrower, it is not an infraction.\n\n\t\t18.1.1.4. “Wrapping” – a line between a defensive player’s hands or arms comes within one disc diameter of the thrower’s torso, or any part of the defensive player’s body is above the thrower’s pivot point. However, if this situation is caused solely by movement of the thrower, it is not an infraction.  \n\n\t\t18.1.1.5. "Double Team" –a defensive player other than the marker is within three (3) metres of the thrower\'s pivot point without also guarding another offensive player. However, merely running across this area is not a double team.\n\n\t\t18.1.1.6. “Vision” - a defensive player uses any part of their body to intentionally obstruct the thrower’s vision.')
        await message.channel.send('\n\n\t18.1.2. A marking infraction may be contested by the defence, in which case play stops.\n\t18.1.2.1. If a pass has been completed, a contested or retracted marking infraction must be treated as a violation by the offence, and the disc must be returned to the thrower.\n\t18.1.3. After all marking infractions listed in 18.1.1. that are not contested, the marker must resume the stall count with the number last fully uttered before the call, minus one (1).\n\t18.1.4. The marker may not resume counting until any illegal positioning has been corrected.  To do otherwise is a subsequent marking infraction.\n\t18.1.5. Instead of calling a marking infraction, the thrower may call a marking violation and stop play if; \n\t\t18.1.5.1. the stall count is not corrected,\n\t\t18.1.5.2. there is no stall count,\n\t\t18.1.5.3. there is an egregious marking infraction, or\n\t\t18.1.5.4. there is a pattern of repeated marking infractions.\n\t18.1.6. If a marking infraction, or a marking violation, is called and the thrower also attempts a pass before, during or after the call, the call has no consequences (unless 18.1.2.1 applies) and if the pass is incomplete, then the turnover stands.')  

      elif message.content.startswith('!18.2'):
        await message.channel.send('18.2. “Travel” Infractions: \n\t18.2.1. The thrower may attempt a pass at any time as long as they are entirely in-bounds or have established an in-bounds pivot point.\n\t\t18.2.1.1. However an in-bounds player who catches a pass while airborne may attempt a pass prior to contacting the ground.\n\t18.2.2. After catching the disc, and landing in-bounds, the thrower must reduce speed as quickly as possible, without changing direction, until they have established a pivot point.\n\t\t18.2.2.1. However if a player catches the disc while running or jumping the player may release a pass without attempting to reduce speed and without establishing a pivot point, provided that:\n\t\t\t18.2.2.1.1. they do not change direction or increase speed until they release the pass; and\n\t\t18.2.2.1.2. a maximum of two additional points of contact with the ground are made after the catch and before they release the pass.\n\t18.2.3. The thrower may move in any direction (pivot) only by establishing a “pivot point”, which is a specific point on the ground with which one part of their body remains in constant contact until the disc is thrown.\n\t18.2.4. A thrower who is not standing can use any part of their body as the pivot point.\n\t\t18.2.4.1. If they stand up it is not a travel, but only if a pivot point is established at the same location.')
        await message.channel.send('\t18.2.5. A travel infraction occurs if: \n\t\t18.2.5.1. the thrower establishes a pivot point at an incorrect location, including by not reducing speed as quickly as possible after a catch, or changing direction after a catch;\n\t\t18.2.5.2. the thrower releases a pass in breach of 18.2.2.1;\n\t\t18.2.5.3. anytime the thrower must move to a specified location, the thrower does not establish a pivot point before a wind-up or throwing action begins;\n\t\t18.2.5.4. the thrower fails to keep the established pivot point until releasing the disc;\n\t\t18.2.5.5. a player intentionally bobbles, fumbles or delays the disc to themselves, for the sole purpose of moving in a specific direction.\n\t18.2.6. After an accepted travel infraction is called ("travel"), play does not stop.\n\t\t18.2.6.1. The thrower establishes a pivot point at the correct location, as indicated by the player who called the travel.  This must occur without delay from either player involved.\n\t\t18.2.6.2. Any stall count is paused, and the thrower may not throw the disc, until a pivot point is established at the correct location.\n\t\t18.2.6.3. The marker does not need to say “Stalling” before resuming the stall count.\n\t18.2.7. If, after a travel infraction but before correcting the pivot point, the thrower throws a completed pass, the defensive team may call a travel violation.  Play stops and the disc is returned to the thrower. The thrower must return to the location occupied at the time of the infraction. Play must restart with a check.\n\t18.2.8. If, after a travel infraction, the thrower throws an incomplete pass, play continues.\n\t18.2.9. After a contested travel infraction where the thrower has not released the disc, play stops.')  

      elif message.content.startswith('!18.3'):   
        await message.channel.send('18.3. “Pick” Violations:\n\t18.3.1. If a defensive player is guarding one offensive player and they are prevented from moving towards/with that player by another player, that defensive player may call “Pick”. However it is not a pick if both the player being guarded and the obstructing player are making a play on the disc.\n\t\t18.3.1.1. Prior to making the "Pick" call, the defender may delay the call up to two (2) seconds to determine if the obstruction will affect the play.\n\t18.3.2. If play has stopped, the obstructed player may move to the agreed position they would have otherwise occupied if the obstruction had not occurred, unless specified otherwise.\n\t18.3.3. All players should take reasonable efforts to avoid the occurrence of picks.\n\t\t18.3.3.1. During any stoppage opposing players may agree to slightly adjust their locations to avoid potential picks.')  

      else:
        await message.channel.send('18. Infractions and Violations\n‎‎‏‏‎ ‎  ‎')      
        await message.channel.send('18.1. Marking Infractions:\n\n\t18.1.1. Marking infractions include the following:\n\n\t\t18.1.1.1. “Fast Count” – the marker:\n\t\t\t18.1.1.1.1. starts or continues the stall count illegally,\n\t\t\t18.1.1.1.2. does not start or restart the stall count with the word “Stalling”,\n\t\t\t18.1.1.1.3. counts in less than one second intervals,\n\t\t\t18.1.1.1.4. does not correctly reduce or reset the stall count when required, or\n\t\t\t18.1.1.1.5. does not start the stall count from the correct number.\n\n\t\t18.1.1.2. “Straddle” – a line between a defensive player’s feet comes within one disc diameter of the thrower’s pivot point.\n\n\t\t18.1.1.3. “Disc Space” – any part of a defensive player is less than one disc diameter away from the torso of the thrower.  However, if this situation is caused solely by movement of the thrower, it is not an infraction.\n\n\t\t18.1.1.4. “Wrapping” – a line between a defensive player’s hands or arms comes within one disc diameter of the thrower’s torso, or any part of the defensive player’s body is above the thrower’s pivot point. However, if this situation is caused solely by movement of the thrower, it is not an infraction.  \n\n\t\t18.1.1.5. "Double Team" –a defensive player other than the marker is within three (3) metres of the thrower\'s pivot point without also guarding another offensive player. However, merely running across this area is not a double team.\n\n\t\t18.1.1.6. “Vision” - a defensive player uses any part of their body to intentionally obstruct the thrower’s vision.')  
        await message.channel.send('\n\n\t18.1.2. A marking infraction may be contested by the defence, in which case play stops.\n\t18.1.2.1. If a pass has been completed, a contested or retracted marking infraction must be treated as a violation by the offence, and the disc must be returned to the thrower.\n\t18.1.3. After all marking infractions listed in 18.1.1. that are not contested, the marker must resume the stall count with the number last fully uttered before the call, minus one (1).\n\t18.1.4. The marker may not resume counting until any illegal positioning has been corrected.  To do otherwise is a subsequent marking infraction.\n\t18.1.5. Instead of calling a marking infraction, the thrower may call a marking violation and stop play if; \n\t\t18.1.5.1. the stall count is not corrected,\n\t\t18.1.5.2. there is no stall count,\n\t\t18.1.5.3. there is an egregious marking infraction, or\n\t\t18.1.5.4. there is a pattern of repeated marking infractions.\n\t18.1.6. If a marking infraction, or a marking violation, is called and the thrower also attempts a pass before, during or after the call, the call has no consequences (unless 18.1.2.1 applies) and if the pass is incomplete, then the turnover stands.\n‎‎‏‏‎ ‎ ')  
        await message.channel.send('18.2. “Travel” Infractions: \n\t18.2.1. The thrower may attempt a pass at any time as long as they are entirely in-bounds or have established an in-bounds pivot point.\n\t\t18.2.1.1. However an in-bounds player who catches a pass while airborne may attempt a pass prior to contacting the ground.\n\t18.2.2. After catching the disc, and landing in-bounds, the thrower must reduce speed as quickly as possible, without changing direction, until they have established a pivot point.\n\t\t18.2.2.1. However if a player catches the disc while running or jumping the player may release a pass without attempting to reduce speed and without establishing a pivot point, provided that:\n\t\t\t18.2.2.1.1. they do not change direction or increase speed until they release the pass; and\n\t\t18.2.2.1.2. a maximum of two additional points of contact with the ground are made after the catch and before they release the pass.\n\t18.2.3. The thrower may move in any direction (pivot) only by establishing a “pivot point”, which is a specific point on the ground with which one part of their body remains in constant contact until the disc is thrown.\n\t18.2.4. A thrower who is not standing can use any part of their body as the pivot point.\n\t\t18.2.4.1. If they stand up it is not a travel, but only if a pivot point is established at the same location.')
        await message.channel.send('18.2.5. A travel infraction occurs if: \n\t\t18.2.5.1. the thrower establishes a pivot point at an incorrect location, including by not reducing speed as quickly as possible after a catch, or changing direction after a catch;\n\t\t18.2.5.2. the thrower releases a pass in breach of 18.2.2.1;\n\t\t18.2.5.3. anytime the thrower must move to a specified location, the thrower does not establish a pivot point before a wind-up or throwing action begins;\n\t\t18.2.5.4. the thrower fails to keep the established pivot point until releasing the disc;\n\t\t18.2.5.5. a player intentionally bobbles, fumbles or delays the disc to themselves, for the sole purpose of moving in a specific direction.\n\t18.2.6. After an accepted travel infraction is called ("travel"), play does not stop.\n\t\t18.2.6.1. The thrower establishes a pivot point at the correct location, as indicated by the player who called the travel.  This must occur without delay from either player involved.\n\t\t18.2.6.2. Any stall count is paused, and the thrower may not throw the disc, until a pivot point is established at the correct location.\n\t\t18.2.6.3. The marker does not need to say “Stalling” before resuming the stall count.\n\t18.2.7. If, after a travel infraction but before correcting the pivot point, the thrower throws a completed pass, the defensive team may call a travel violation.  Play stops and the disc is returned to the thrower. The thrower must return to the location occupied at the time of the infraction. Play must restart with a check.\n\t18.2.8. If, after a travel infraction, the thrower throws an incomplete pass, play continues.\n\t18.2.9. After a contested travel infraction where the thrower has not released the disc, play stops.\n‎‎‏‏‎ ‎')  
        await message.channel.send('18.3. “Pick” Violations:\n\t18.3.1. If a defensive player is guarding one offensive player and they are prevented from moving towards/with that player by another player, that defensive player may call “Pick”. However it is not a pick if both the player being guarded and the obstructing player are making a play on the disc.\n\t\t18.3.1.1. Prior to making the "Pick" call, the defender may delay the call up to two (2) seconds to determine if the obstruction will affect the play.\n\t18.3.2. If play has stopped, the obstructed player may move to the agreed position they would have otherwise occupied if the obstruction had not occurred, unless specified otherwise.\n\t18.3.3. All players should take reasonable efforts to avoid the occurrence of picks.\n\t\t18.3.3.1. During any stoppage opposing players may agree to slightly adjust their locations to avoid potential picks.\n‎‎‏‏‎ ‎')



    if message.content.startswith('!19.'):

      if message.content.startswith('!19.1'):
        await message.channel.send('19.1. Injury Stoppage\n\t19.1.1. An injury stoppage, “Injury”, may be called by the injured player, or by any player on the injured player’s team.\n\t19.1.2. If the injury was not caused by an opponent, the player must choose either to be substituted, or to charge their own team with a time-out. \n\t19.1.3. If the injury was caused by an opponent the player may choose to stay or to be substituted.\n\t19.1.4. If the injured player had established possession of the disc, and the player has dropped the disc due to the injury, that player retains possession of the disc.\n\t19.1.5. The injury stoppage is considered to have been called at the time of the injury, unless the injured player chooses to continue play before the stoppage is called.\n\t19.1.6. If the disc was in the air when the injury stoppage was called, play continues until either a player establishes possesion, or the disc hits the ground. If the injury is not the result of a foul by an opponent, the completion or turnover stands, and play restarts there after the stoppage.')  

      elif message.content.startswith('!19.2'):
        await message.channel.send('19.2. Technical Stoppage\n\t19.2.1. Any player who recognises a condition that endangers players, including if a player has an open or bleeding wound, should call a technical stoppage by calling “technical” or “stop”. Play must stop immediately. \n\t\t19.2.1.1. A team-mate, coach, or designated official, should actively alert players to any condition that endangers players.\n\t\t19.2.1.2. A player who has an issue regarding an open or bleeding wound has seventy (70) seconds to effectively address the issue. If they need additional time to address the issue, they must choose either to be substituted, or to charge their own team with a time-out.\n\t19.2.2. The thrower may call a technical stoppage during play to replace a severely damaged disc. \n\t19.2.3. After a technical stoppage called while the disc is in the air, or if play has continued unknowingly:\n\t\t19.2.3.1. If the call or issue did not affect play, the completion or turnover stands, and play restarts there;\n\t\t19.2.3.2. If the call or issue did affect the play, the disc goes back to the thrower.')  

      elif message.content.startswith('!19.3'):   
        await message.channel.send('19.3. If a player is substituted after an injury, or due to illegal or faulty equipment, the opposing team may also choose to substitute one player.\n\t19.3.1. Substitute players take on the full state (location, possession, stall count etc) of the player they are substituting and may make a call on their behalf.')  

      else:
        await message.channel.send('19. Safety Stoppages\n‎‎‏‏‎ ‎  ‎')        
        await message.channel.send('19.1. Injury Stoppage\n\t19.1.1. An injury stoppage, “Injury”, may be called by the injured player, or by any player on the injured player’s team.\n\t19.1.2. If the injury was not caused by an opponent, the player must choose either to be substituted, or to charge their own team with a time-out. \n\t19.1.3. If the injury was caused by an opponent the player may choose to stay or to be substituted.\n\t19.1.4. If the injured player had established possession of the disc, and the player has dropped the disc due to the injury, that player retains possession of the disc.\n\t19.1.5. The injury stoppage is considered to have been called at the time of the injury, unless the injured player chooses to continue play before the stoppage is called.\n\t19.1.6. If the disc was in the air when the injury stoppage was called, play continues until either a player establishes possesion, or the disc hits the ground. If the injury is not the result of a foul by an opponent, the completion or turnover stands, and play restarts there after the stoppage.\n‎‎‏‏‎ ‎ ')  
        await message.channel.send('19.2. Technical Stoppage\n\t19.2.1. Any player who recognises a condition that endangers players, including if a player has an open or bleeding wound, should call a technical stoppage by calling “technical” or “stop”. Play must stop immediately. \n\t\t19.2.1.1. A team-mate, coach, or designated official, should actively alert players to any condition that endangers players.\n\t\t19.2.1.2. A player who has an issue regarding an open or bleeding wound has seventy (70) seconds to effectively address the issue. If they need additional time to address the issue, they must choose either to be substituted, or to charge their own team with a time-out.\n\t19.2.2. The thrower may call a technical stoppage during play to replace a severely damaged disc. \n\t19.2.3. After a technical stoppage called while the disc is in the air, or if play has continued unknowingly:\n\t\t19.2.3.1. If the call or issue did not affect play, the completion or turnover stands, and play restarts there;\n\t\t19.2.3.2. If the call or issue did affect the play, the disc goes back to the thrower.\n‎‎‏‏‎ ‎')  
        await message.channel.send('19.3. If a player is substituted after an injury, or due to illegal or faulty equipment, the opposing team may also choose to substitute one player.\n\t19.3.1. Substitute players take on the full state (location, possession, stall count etc) of the player they are substituting and may make a call on their behalf.\n‎‎‏‏‎ ‎')



    if message.content.startswith('!20.'):

      if message.content.startswith('!20.1'):
        await message.channel.send('20.1. The player calling a time-out must form a "T" with their hands, or with one hand and the disc, and should call "time-out" to opposition players.')  

      elif message.content.startswith('!20.2'):
        await message.channel.send('20.2. After the start of a point and before both teams have signalled readiness, a player from either team may call a time-out. The time-out extends the time between the start of the point and subsequent pull by seventy-five (75) seconds.')  

      elif message.content.startswith('!20.3'):   
        await message.channel.send('20.3. After the pull only a thrower with possession of the disc may call a time-out. The time-out starts when the “T” is formed, and lasts seventy-five (75) seconds. After such a time-out: \n\t20.3.1. Substitutions are not allowed, except for injury.\n\t20.3.2. Play is restarted at the pivot location.\n\t20.3.3. The thrower must remain the same.\n\t20.3.4. All other offensive players must establish a stationary position, at any location.\n\t20.3.5. Once the offensive players have selected positions, defensive players must then establish a stationary position, at any location\n\t20.3.6. The stall count restarts at maximum nine (9). However if the marker has been switched, the stall count restarts at “Stalling one (1)”.')  

      elif message.content.startswith('!20.4'): 
       await message.channel.send('20.4. If the thrower attempts to call a time-out while play i live and when their team has no remaining time-outs, play is stopped. The marker must add two (2) seconds to the stall count they would have restarted play on before restarting play with a check. If this results in a stall count of ten (10) or above, this is a "stall-out" turnover.')  

      else:
        await message.channel.send('8. State of Play\n‎‎‏‏‎ ‎  ‎')        
        await message.channel.send('20.1. The player calling a time-out must form a "T" with their hands, or with one hand and the disc, and should call "time-out" to opposition players.\n‎‎‏‏‎ ‎ ')  
        await message.channel.send('20.2. After the start of a point and before both teams have signalled readiness, a player from either team may call a time-out. The time-out extends the time between the start of the point and subsequent pull by seventy-five (75) seconds.\n‎‎‏‏‎ ‎')  
        await message.channel.send('20.3. After the pull only a thrower with possession of the disc may call a time-out. The time-out starts when the “T” is formed, and lasts seventy-five (75) seconds. After such a time-out: \n\t20.3.1. Substitutions are not allowed, except for injury.\n\t20.3.2. Play is restarted at the pivot location.\n\t20.3.3. The thrower must remain the same.\n\t20.3.4. All other offensive players must establish a stationary position, at any location.\n\t20.3.5. Once the offensive players have selected positions, defensive players must then establish a stationary position, at any location\n\t20.3.6. The stall count restarts at maximum nine (9). However if the marker has been switched, the stall count restarts at “Stalling one (1)”.\n‎‎‏‏‎ ‎')  
        await message.channel.send('20.4. If the thrower attempts to call a time-out while play i live and when their team has no remaining time-outs, play is stopped. The marker must add two (2) seconds to the stall count they would have restarted play on before restarting play with a check. If this results in a stall count of ten (10) or above, this is a "stall-out" turnover.\n‎‎‏‏‎ ‎')



    if message.content.startswith('!dangerous play'):
        await message.channel.send('17.1. Dangerous Play:\n\n\t17.1.1. Actions demonstrating reckless disregard for the safety of fellow players, or posing significant risk of injury to fellow players, or other dangerously aggressive behaviours, are considered dangerous play and must be treated as a foul, regardless of whether or when contact occurs. This rule is not superseded by any other foul rule. If the dangerous play call is accepted, this must be treated as the most relevant foul from Section 17.') 

    if message.content.startswith('!receiving foul'):
        await message.channel.send('17.2. Receiving Fouls:\n\n\t17.2.1. A Receiving Foul occurs when a player initiates non-minor contact with an opponent before, while, or directly after, either player makes a play on the disc. \n\t\t17.2.1.1. Contact with an opponent’s arms or hands, that occurs after the disc has been caught, or after the opponent can no longer make a play on the disc, is not a sufficient basis for a foul, but should be avoided (excluding contact related to Section 17.1 and 17.3).\n\n\t17.2.2. After an accepted receiving foul the fouled player gains possession at the location of the breach, even if that location is in an end zone, and play restarts with a check. If, after the check, 14.3 applies, the stall count can not be started until a pivot point is established at the nearest location on the goal line. If the foul is contested, the disc is returned to the thrower.')  

    if message.content.startswith('!strip'):
        await message.channel.send('17.3. Strip Fouls:\n\n\t17.3.1. A Strip Foul occurs when an opponent fouls a player and that causes the player to drop a disc they caught or to lose possession of the disc.\n\n\t17.3.2. If the reception would have otherwise been a goal, and the foul is uncontested, a goal is awarded.')  

    if message.content.startswith('!blocking'):
        await message.channel.send('17.4. Blocking Fouls:\n\n\t17.4.1. A Blocking Foul occurs when a player takes a position that an opponent moving in a legal manner will be unable to avoid, taking into account the opponents expected position based on their established speed and direction, and non-minor contact results. This is to be treated as either a receiving foul or an indirect foul, whichever is applicable.')  

    if message.content.startswith('!force-out'):
        await message.channel.send('17.5. Force-out Fouls:\n\n\t17.5.1. A Force-out Foul occurs when a receiver is in the process of establishing possession of the disc, and is fouled by a defensive player before establishing possession, and the contact caused the receiver:\n\t\t17.5.1.1. to become out-of-bounds instead of in-bounds; or\n\t\t17.5.1.2. to catch the disc in the central zone instead of their attacking end zone.\n\n\t17.5.2. If the receiver would have caught the disc in their attacking end zone, it is a goal;\n\n\t17.5.3. If the force-out foul is contested, the disc is returned to the thrower if the receiver became out-of-bounds, otherwise the disc stays with the receiver.')  

    if message.content.startswith('!defensive foul'):
        await message.channel.send('17.6. Defensive Throwing (Marking) Fouls: \n\n\t17.6.1. A Defensive Throwing Foul occurs when:\n\t\t17.6.1.1. A defensive player is illegally positioned (Section 18.1), and there is non-minor contact between the illegally positioned defensive player and the thrower; or\n\t\t17.6.1.2. A defensive player initiates non-minor contact with the thrower, or there is non-minor contact resulting from the thrower and the defender both vying for the same unoccupied position, prior to the release.\n\t\t17.6.1.3. If a Defensive Throwing Foul occurs prior to the thrower releasing the disc and not during the throwing motion, the thrower may choose to call a contact infraction, by calling “Contact”. After a contact infraction that is not contested, play does not stop and the marker must resume the stall count at one (1).')  

    if message.content.startswith('!offensive foul'):
        await message.channel.send('17.7. Offensive Throwing (Thrower) Fouls:\n\n\t17.7.1. An Offensive Throwing Foul occurs when the thrower is solely responsible for initiating non-minor contact with a defensive player who is in a legal position. \n\n\t17.7.2. Contact occurring during the thrower\'s follow through is not a sufficient basis for a foul, but should be avoided.') 

    if message.content.startswith('!indirect foul'):
        await message.channel.send('17.8. Indirect Fouls:\n\n\t17.8.1. An Indirect Foul occurs when there is non-minor contact between a receiver and a defensive player that does not directly affect an attempt to make a play on the disc. \n\n\t17.8.2. If the foul is accepted the fouled player may make up any positional disadvantage caused by the foul.') 

    if message.content.startswith('!off setting foul'):
        await message.channel.send('17.9. Offsetting Fouls:\n\n\t17.9.1. If accepted fouls are called by offensive and defensive players on the same play, these are offsetting fouls, and the disc must be returned to the last non-disputed thrower.\n\n\t17.9.2. If there is non-minor contact that is caused by two or more opposing players moving towards a single point simultaneously, this must be treated as offsetting fouls. \n\t\t17.9.2.1. However if this occurs after the disc has been caught, or after the relevant player/s involved can no longer make a play on the disc, this must be treated as an Indirect Foul (excluding contact related to Section 17.1).') 

    if message.content.startswith('!marking infraction'):
        await message.channel.send('18.1. Marking Infractions:\n\n\t18.1.1. Marking infractions include the following:\n\n\t\t18.1.1.1. “Fast Count” – the marker:\n\t\t\t18.1.1.1.1. starts or continues the stall count illegally,\n\t\t\t18.1.1.1.2. does not start or restart the stall count with the word “Stalling”,\n\t\t\t18.1.1.1.3. counts in less than one second intervals,\n\t\t\t18.1.1.1.4. does not correctly reduce or reset the stall count when required, or\n\t\t\t18.1.1.1.5. does not start the stall count from the correct number.\n\n\t\t18.1.1.2. “Straddle” – a line between a defensive player’s feet comes within one disc diameter of the thrower’s pivot point.\n\n\t\t18.1.1.3. “Disc Space” – any part of a defensive player is less than one disc diameter away from the torso of the thrower.  However, if this situation is caused solely by movement of the thrower, it is not an infraction.\n\n\t\t18.1.1.4. “Wrapping” – a line between a defensive player’s hands or arms comes within one disc diameter of the thrower’s torso, or any part of the defensive player’s body is above the thrower’s pivot point. However, if this situation is caused solely by movement of the thrower, it is not an infraction.  \n\n\t\t18.1.1.5. "Double Team" –a defensive player other than the marker is within three (3) metres of the thrower\'s pivot point without also guarding another offensive player. However, merely running across this area is not a double team.\n\n\t\t18.1.1.6. “Vision” - a defensive player uses any part of their body to intentionally obstruct the thrower’s vision.')  
        await message.channel.send('\n\n\t18.1.2. A marking infraction may be contested by the defence, in which case play stops.\n\t18.1.2.1. If a pass has been completed, a contested or retracted marking infraction must be treated as a violation by the offence, and the disc must be returned to the thrower.\n\t18.1.3. After all marking infractions listed in 18.1.1. that are not contested, the marker must resume the stall count with the number last fully uttered before the call, minus one (1).\n\t18.1.4. The marker may not resume counting until any illegal positioning has been corrected.  To do otherwise is a subsequent marking infraction.\n\t18.1.5. Instead of calling a marking infraction, the thrower may call a marking violation and stop play if; \n\t\t18.1.5.1. the stall count is not corrected,\n\t\t18.1.5.2. there is no stall count,\n\t\t18.1.5.3. there is an egregious marking infraction, or\n\t\t18.1.5.4. there is a pattern of repeated marking infractions.\n\t18.1.6. If a marking infraction, or a marking violation, is called and the thrower also attempts a pass before, during or after the call, the call has no consequences (unless 18.1.2.1 applies) and if the pass is incomplete, then the turnover stands.\n‎‎‏‏‎ ‎ ')  

    if message.content.startswith('!fast count'):
        await message.channel.send('18.1.1.1. “Fast Count” – the marker:\n\tt18.1.1.1.1. starts or continues the stall count illegally,\n\t18.1.1.1.2. does not start or restart the stall count with the word “Stalling”,\n\t18.1.1.1.3. counts in less than one second intervals,\n\t18.1.1.1.4. does not correctly reduce or reset the stall count when required, or\n\t18.1.1.1.5. does not start the stall count from the correct number.')  

    if message.content.startswith('!straddle'):
        await message.channel.send('18.1.1.2. “Straddle” – a line between a defensive player’s feet comes within one disc diameter of the thrower’s pivot point.')  

    if message.content.startswith('!disc space'):
        await message.channel.send('18.1.1.3. “Disc Space” – any part of a defensive player is less than one disc diameter away from the torso of the thrower.  However, if this situation is caused solely by movement of the thrower, it is not an infraction.')  

    if message.content.startswith('!wrapping'):
        await message.channel.send('18.1.1.4. “Wrapping” – a line between a defensive player’s hands or arms comes within one disc diameter of the thrower’s torso, or any part of the defensive player’s body is above the thrower’s pivot point. However, if this situation is caused solely by movement of the thrower, it is not an infraction.')  

    if message.content.startswith('!double team'):
        await message.channel.send('18.1.1.5. "Double Team" –a defensive player other than the marker is within three (3) metres of the thrower\'s pivot point without also guarding another offensive player. However, merely running across this area is not a double team.')  

    if message.content.startswith('!vision'):
        await message.channel.send('18.1.1.6. “Vision” - a defensive player uses any part of their body to intentionally obstruct the thrower’s vision.')  

    if message.content.startswith('!travel'):
        await message.channel.send('18.2. “Travel” Infractions: \n\t18.2.1. The thrower may attempt a pass at any time as long as they are entirely in-bounds or have established an in-bounds pivot point.\n\t\t18.2.1.1. However an in-bounds player who catches a pass while airborne may attempt a pass prior to contacting the ground.\n\t18.2.2. After catching the disc, and landing in-bounds, the thrower must reduce speed as quickly as possible, without changing direction, until they have established a pivot point.\n\t\t18.2.2.1. However if a player catches the disc while running or jumping the player may release a pass without attempting to reduce speed and without establishing a pivot point, provided that:\n\t\t\t18.2.2.1.1. they do not change direction or increase speed until they release the pass; and\n\t\t18.2.2.1.2. a maximum of two additional points of contact with the ground are made after the catch and before they release the pass.\n\t18.2.3. The thrower may move in any direction (pivot) only by establishing a “pivot point”, which is a specific point on the ground with which one part of their body remains in constant contact until the disc is thrown.\n\t18.2.4. A thrower who is not standing can use any part of their body as the pivot point.\n\t\t18.2.4.1. If they stand up it is not a travel, but only if a pivot point is established at the same location.')
        await message.channel.send('18.2.5. A travel infraction occurs if: \n\t\t18.2.5.1. the thrower establishes a pivot point at an incorrect location, including by not reducing speed as quickly as possible after a catch, or changing direction after a catch;\n\t\t18.2.5.2. the thrower releases a pass in breach of 18.2.2.1;\n\t\t18.2.5.3. anytime the thrower must move to a specified location, the thrower does not establish a pivot point before a wind-up or throwing action begins;\n\t\t18.2.5.4. the thrower fails to keep the established pivot point until releasing the disc;\n\t\t18.2.5.5. a player intentionally bobbles, fumbles or delays the disc to themselves, for the sole purpose of moving in a specific direction.\n\t18.2.6. After an accepted travel infraction is called ("travel"), play does not stop.\n\t\t18.2.6.1. The thrower establishes a pivot point at the correct location, as indicated by the player who called the travel.  This must occur without delay from either player involved.\n\t\t18.2.6.2. Any stall count is paused, and the thrower may not throw the disc, until a pivot point is established at the correct location.\n\t\t18.2.6.3. The marker does not need to say “Stalling” before resuming the stall count.\n\t18.2.7. If, after a travel infraction but before correcting the pivot point, the thrower throws a completed pass, the defensive team may call a travel violation.  Play stops and the disc is returned to the thrower. The thrower must return to the location occupied at the time of the infraction. Play must restart with a check.\n\t18.2.8. If, after a travel infraction, the thrower throws an incomplete pass, play continues.\n\t18.2.9. After a contested travel infraction where the thrower has not released the disc, play stops.\n‎‎‏‏‎ ‎') 

    if message.content.startswith('!pick'):
        await message.channel.send('18.3. “Pick” Violations:\n\t18.3.1. If a defensive player is guarding one offensive player and they are prevented from moving towards/with that player by another player, that defensive player may call “Pick”. However it is not a pick if both the player being guarded and the obstructing player are making a play on the disc.\n\t\t18.3.1.1. Prior to making the "Pick" call, the defender may delay the call up to two (2) seconds to determine if the obstruction will affect the play.\n\t18.3.2. If play has stopped, the obstructed player may move to the agreed position they would have otherwise occupied if the obstruction had not occurred, unless specified otherwise.\n\t18.3.3. All players should take reasonable efforts to avoid the occurrence of picks.\n\t\t18.3.3.1. During any stoppage opposing players may agree to slightly adjust their locations to avoid potential picks.\n‎‎‏‏‎ ‎')

    if message.content.startswith('!new rules'):
        await message.channel.send('New Rules and Changes\n\n1.2.1\n7.5\n9.3.1\n9.5\n9.5.4.1\n10.7\n12.1\n12.5\n12.6\n12.7\n13.4\n15.1.1\n15.5.1\n15.12\n16.2\n16.2.4.1\n16.3\n17.2.1\n17.3.1\n17.5.1\n17.9.2.1\n18.1.1.2\n18.1.1.4\n18.1.2.1\n18.2.2.1\n18.2.5.3\n18.2.6.3\n19.2.1\n19.2.1.1')




keep_alive()

client.run(os.getenv('TOKEN'))
