% ============================================
% TASK 3: PROLOG FAMILY TREE
% ============================================
% This file defines family relationships including:
% grandparents, parents, children, grandchildren,
% cousins, uncles, and aunts
% ============================================

% ============================================
% PART A & B: Basic Prolog Setup and Testing
% ============================================

% Define family facts
% Format: parent(Parent, Child)

% Generation 1 (Grandparents)
parent(john_donny, mary_smith).
parent(jane_donny, mary_smith).
parent(john_donny, robert_johnson).
parent(jane_donny, robert_johnson).

parent(robert_brown, alice_wilson).
parent(susan_brown, alice_wilson).
parent(robert_brown, charles_davis).
parent(susan_brown, charles_davis).

% Generation 2 (Parents)
parent(mary_smith, tom_wilson).
parent(robert_johnson, tom_wilson).
parent(mary_smith, emma_jones).
parent(robert_johnson, emma_jones).

parent(alice_wilson, michael_brown).
parent(charles_davis, michael_brown).
parent(alice_wilson, sarah_martin).
parent(charles_davis, sarah_martin).

% Generation 3 (Children)
parent(tom_wilson, olivia_white).
parent(emma_jones, olivia_white).
parent(tom_wilson, liam_green).
parent(emma_jones, liam_green).

parent(michael_brown, sophia_black).
parent(sarah_martin, sophia_black).
parent(michael_brown, noah_taylor).
parent(sarah_martin, noah_taylor).

% Additional relationships
parent(tom_wilson, isabella_anderson).
parent(emma_jones, isabella_anderson).

% Define gender for proper relationship determination
male(john_donny).
male(robert_johnson).
male(robert_brown).
male(charles_davis).
male(tom_wilson).
male(michael_brown).
male(liam_green).
male(noah_taylor).

female(jane_donny).
female(mary_smith).
female(susan_brown).
female(alice_wilson).
female(emma_jones).
female(sarah_martin).
female(olivia_white).
female(sophia_black).
female(isabella_anderson).

% ============================================
% BASIC RELATIONSHIP RULES
% ============================================

% Child relationship
child(X, Y) :- parent(Y, X).

% Grandparent relationship
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

% Grandchild relationship
grandchild(X, Y) :- grandparent(Y, X).

% Sibling relationship (sharing at least one parent)
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Brother relationship
brother(X, Y) :- male(X), sibling(X, Y).

% Sister relationship
sister(X, Y) :- female(X), sibling(X, Y).

% ============================================
% ADVANCED RELATIONSHIP RULES
% ============================================

% Uncle - brother of a parent
uncle(X, Y) :- male(X), parent(Z, Y), sibling(X, Z).

% Aunt - sister of a parent
aunt(X, Y) :- female(X), parent(Z, Y), sibling(X, Z).

% Cousin relationship
% First cousins share grandparents
cousin(X, Y) :- grandparent(Z, X), grandparent(Z, Y), X \= Y, \+ sibling(X, Y).

% First cousin once removed (different generations)
cousin_once_removed(X, Y) :-
    (grandparent(Z, X), parent(X, W), grandparent(Z, W));  % X is parent of W
    (grandparent(Z, Y), parent(Y, W), grandparent(Z, W)).   % Y is parent of W

% ============================================
% FAMILY TREE QUERIES AND TESTING
% ============================================

% Test all relationships
test_relationships :-
    write('========================================'), nl,
    write('FAMILY TREE RELATIONSHIP TESTS'), nl,
    write('========================================'), nl, nl,
    
    % Test parents
    write('PARENTS:'), nl,
    findall(P-C, parent(P, C), ParentList),
    print_list(ParentList),
    nl,
    
    % Test grandparents
    write('GRANDPARENTS:'), nl,
    findall(GP-GC, grandparent(GP, GC), GrandparentList),
    print_list(GrandparentList),
    nl,
    
    % Test siblings
    write('SIBLINGS:'), nl,
    findall(X-Y, sibling(X, Y), SiblingList),
    print_pair_list(SiblingList),
    nl,
    
    % Test uncles
    write('UNCLES:'), nl,
    findall(U-N, uncle(U, N), UncleList),
    print_pair_list(UncleList),
    nl,
    
    % Test aunts
    write('AUNTS:'), nl,
    findall(A-N, aunt(A, N), AuntList),
    print_pair_list(AuntList),
    nl,
    
    % Test cousins
    write('COUSINS:'), nl,
    findall(C1-C2, cousin(C1, C2), CousinList),
    print_pair_list(CousinList),
    nl,
    
    write('All tests completed!'), nl.

% Helper predicate to print lists
print_list([]).
print_list([H|T]) :-
    write(H), nl,
    print_list(T).

print_pair_list([]).
print_pair_list([X-Y|T]) :-
    write(X), write(' is '), write(Y), write('\'s '), 
    (Y = X -> write('sibling') ; true),
    nl,
    print_pair_list(T).

% Specific queries for demonstration
run_queries :-
    write('========================================'), nl,
    write('SPECIFIC FAMILY QUERIES'), nl,
    write('========================================'), nl, nl,
    
    % Find grandparents of Olivia
    write('1. Grandparents of Olivia White:'), nl,
    findall(GP, grandparent(GP, olivia_white), GPList),
    write(GPList), nl, nl,
    
    % Find children of Mary Smith
    write('2. Children of Mary Smith:'), nl,
    findall(C, parent(mary_smith, C), ChildrenList),
    write(ChildrenList), nl, nl,
    
    % Find siblings of Tom Wilson
    write('3. Siblings of Tom Wilson:'), nl,
    findall(S, sibling(S, tom_wilson), SiblingList),
    write(SiblingList), nl, nl,
    
    % Find uncles of Olivia White
    write('4. Uncles of Olivia White:'), nl,
    findall(U, uncle(U, olivia_white), UncleList),
    write(UncleList), nl, nl,
    
    % Find aunts of Olivia White
    write('5. Aunts of Olivia White:'), nl,
    findall(A, aunt(A, olivia_white), AuntList),
    write(AuntList), nl, nl,
    
    % Find cousins of Sophia Black
    write('6. Cousins of Sophia Black:'), nl,
    findall(C, cousin(C, sophia_black), CousinList),
    write(CousinList), nl, nl,
    
    write('========================================'), nl.

% Main execution
main :-
    write('FAMILY TREE PROLOG PROGRAM'), nl,
    write('Created for CCS 2226 Task 3'), nl,
    write('========================================'), nl,
    test_relationships,
    run_queries.