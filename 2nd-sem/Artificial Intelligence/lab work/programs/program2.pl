% Program to check whether 7 is greater than 5

greater_check(A, B) :-
    A > B,
    format('~w is greater than ~w~n', [A, B]).

greater_check(A, B) :-
    A =< B,
    format('~w is not greater than ~w~n', [A, B]).