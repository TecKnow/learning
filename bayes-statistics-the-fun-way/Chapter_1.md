#  Chapter 1: Bayesian Thinking and Everyday Reasoning

## Exercises

1.  Rewrite the following statements as equations using the mathematical notation you learned in this chapter: 
    * The probability of rain is low 
    * The probability of rain given that it is cloudy is high 
    * The probability of you having an umbrella given it is raining is much greater than the probability of you having an umbrella in general.

2.  Organize the data you observe in the following scenario into a mathetmatical notation, using the techniques we've covered in this
    chapter.  Then come up with a hypothesis to explain this data:

    >  You come home from work and notice that your front door is open and the side window is broken.  As you walk inside, you immediately notice that your laptop is missing.

3.  The following scenario adds data to the previous one.  Demonstrate how this new information changes your beleifs and come up with a 
    second hypothesis to explain the data, using the notation you've learned in this chapter.
    
    >A neighborhood child runs up to you and appologizes profusely for accidentally throwing a rock through your window.  They claim that they saw the laptop and didn't want it stolen so they opened the front door to gra bit, and your laptop is safe at their house.

## Responses

###  Exercise 1
#### Part 1 

>  The probability of rain is low

Let the following:

1.  $R$ = it is raining
2.  $P(R)$ = the probability that it is raining

Then:

$P(R)$ = low

#### Part 2

>  The probability of rain given that it is cloudy is high

As above, but also let the following:
1.  $C$ = it is cloudy

Then:

$P(R|C)$ = high

#### Part 3

>  The probability of you having an umbrella given it is raining is much greater than the probability of you having an umbrella in general.

As above, but also let the following:

1.  $U$ = You have an umbrella

Then:

$P(U|R) \gg P(U)$

### Exercise 2

>  You come home from work and notice that your front door is open and the side window is broken.  As you walk inside, you immediately notice that your laptop is missing.

Let the following:

1.  $O$ = The front door is open
2.  $B$ = The side window is broken
3.  $M$ = Your laptop is missing
4.  $H_1$ = Your laptop has been stolen 

Then:

$P(O, B, M | H_1)$ = high 

### Exercise 3

>  A neighborhood child runs up to you and appologizes profusely for accidentally throwing a rock through your window.  They claim that 
   they  saw the laptop and didn't want it stolen so they opened the front door to gra bit, and your laptop is safe at their house.

As above, but also let the following:

1. $S$ = A neighborhood child gives the above statement
2. $H_2$ = Your laptop is safe at the neighbor's house

Then:

$P(O, B, M, S| H_2) \gg P(O, B,M, S | H_1)$

$\frac{{P\left( {O,B,M,S|{H_2}} \right)}}{{P\left( {O,B,M,S|{H_1}} \right)}}$ = a large number
