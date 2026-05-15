% ============================================
% ADDITIONAL QUERIES FOR THE FAMILY TREE
% ============================================

% Load the main family tree
:- [family_tree].

% Advanced queries
find_all_grandchildren(X) :-
    write('Grandchildren of '), write(X), write(':'), nl,
    findall(GC, grandchild(GC, X), Grandchildren),
    write(Grandchildren), nl.

find_all_cousins(X) :-
    write('Cousins of '), write(X), write(':'), nl,
    findall(C, cousin(C, X), Cousins),
    write(Cousins), nl.

% Check if two people are related
are_related(X, Y) :-
    (ancestor(X, Y); descendant(X, Y); sibling(X, Y);
     cousin(X, Y); uncle(X, Y); aunt(X, Y);
     grandparent(X, Y); grandchild(X, Y)).

% Find all aunts and uncles of a person
aunts_and_uncles(X, List) :-
    findall(AU, (aunt(AU, X); uncle(AU, X)), List).

% Print entire family tree
print_family_tree :-
    write('FAMILY TREE STRUCTURE'), nl,
    write('====================='), nl,
    write('Generation 1 (Grandparents):'), nl,
    write('  John & Jane Donny'), nl,
    write('  Robert & Susan Brown'), nl, nl,
    
    write('Generation 2 (Parents):'), nl,
    write('  Children of John & Jane: Mary Smith, Robert Johnson'), nl,
    write('  Children of Robert & Susan: Alice Wilson, Charles Davis'), nl, nl,
    
    write('Generation 3 (Adults/Young Adults):'), nl,
    write('  Children of Mary & Robert: Tom Wilson, Emma Jones'), nl,
    write('  Children of Alice & Charles: Michael Brown, Sarah Martin'), nl, nl,
    
    write('Generation 4 (Children):'), nl,
    write('  Children of Tom & Emma: Olivia White, Liam Green, Isabella Anderson'), nl,
    write('  Children of Michael & Sarah: Sophia Black, Noah Taylor'), nl.

% Interactive query system
query_system :-
    write('========================================'), nl,
    write('FAMILY TREE QUERY SYSTEM'), nl,
    write('========================================'), nl,
    write('Available queries:'), nl,
    write('1. parent(X, Y) - X is parent of Y'), nl,
    write('2. child(X, Y) - X is child of Y'), nl,
    write('3. grandparent(X, Y) - X is grandparent of Y'), nl,
    write('4. sibling(X, Y) - X and Y are siblings'), nl,
    write('5. uncle(X, Y) - X is uncle of Y'), nl,
    write('6. aunt(X, Y) - X is aunt of Y'), nl,
    write('7. cousin(X, Y) - X and Y are cousins'), nl,
    write('8. male(X), female(X) - Check gender'), nl,
    write('Type "halt." to exit'), nl,
    write('========================================'), nl.

% Load the query system
:- initialization(query_system).