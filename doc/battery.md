%%
%% This is the main Markdown input file for the BattINFO documentation.
%%
%% Lines starting with a % are pre-processor directives.
%%

%INCLUDE introduction.md

%INCLUDE classes.md


%% %HEADER Individuals       level=1
%% %ALL individuals


%% %HEADER Appendix          level=1
%%
%% %HEADER "The complete taxonomy of Battery Domain Ontology relations"   level=2
%% %BRANCHFIG EMMORelation   caption='The complete taxonomy of Battery Domain Ontology relations.' terminated=0 relations=all edgelabels=0
%%
%% %HEADER "The taxonomy of Battery Domain Ontology classes"     level=2
%% %BRANCHFIG EMMO           caption='The almost complete taxonomy of Battery Domain Ontology classes. Only physical quantities and constants are left out.' terminated=0 relations=isA edgelabels=0 leafs=PhysicalDimension,BaseQuantity,DerivedQuantity,ExactConstant,MeasuredConstant,SIBaseUnit,SISpecialUnit,MetricPrefix,UTF8
