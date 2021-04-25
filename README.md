# Hanab-stats

This is an attempt to rate players on [hanab.live](http://hanab.live/) on a score hunting basis.

## TL;DR

Find [here](https://github.com/Lel0uch-H/hanab-stats/blob/main/output/player_score_summary8.csv) the final output from this scoring methodology in csv format.

## Background

This project is inspired from [Valetta6789&#39;s project](https://github.com/Aigul9/hanabi-stats). The data that I saw there divides the variants in quite a broad manner (Easy, Single Dark, Null, etc.), and looks at the winrates in those variants. Since not every variant is alike (is a &#39;No Variant&#39; game the same as &#39;Omni 6 suits&#39;?), and most players play to score hunt (getting max score on a variant in minimum number of attempts) rather than optimizing for average win rate, I decided to take an alternative approach.

Initially, I planned to use the efficiency metric for each variant along with an additional &quot;cognitive overhead&quot; metric to rate these scores. But on further thought, I realised that would entail a lot of personal bias. The current approach is based entirely on statistics: relying on a players&#39; number of games to reach max score in a variant, compared to the same metric globally.

## Formula used

We define a game type G as the tuple (Variant, Number of players in the game).

For a game type G, let us define the number of players who have won this game type as W(G).

For a player P, let us define the number of game types they have played at least once as A(P).

For a player P, let us define the number of attempts taken to win a game type G for the first time as N(P,G).

For a player P who has attempted but not won a game of type G, let us define the number of failed attempts as F(P,G).

For a player P who has won a game of type G, let us define the score for the player for this game type as:

    S(P,G) = (100/N(P,G)) / (W(G)/
                (   Sum(F(P',G) for all P' who have not won game type G) +
                    (Sum(N(P',G) for all P' who have won game of type G) )
                )
    )

For a player P who has not won a game of type G, S(P,G) = 0.

We define the score for a player S(P) as the average score for that player across all their attempted game types:

    S(P) = Sum (S(P,G) for all G) / (A(P)) 

Note: Due to some outlier data points, S(P,G) is restricted to a maximum value of 300. The player\_score\_summary type 7 has this cap removed.

## Other approaches

There were multiple different approaches that I tried before finalizing on to this one. You can find the approaches in player\_score\_summary1...6.py files. The output can be found in output/player\_score\_summary1...6.csv. The problem with those approaches is that they are either too heavily biased in favor of players who play only easy variants, or too heavily biased in favor of players who have played a large number of variants. The 8th approach seems to be the most balanced one.
