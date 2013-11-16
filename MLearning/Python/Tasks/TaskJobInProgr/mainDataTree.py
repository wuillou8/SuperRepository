#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuiljai
#
# Created:     05/11/2013
# Copyright:   (c) wuiljai 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#http://stackoverflow.com/questions/11479624/is-there-a-way-to-guarantee-hierarchical-output-from-networkx

import myPseudoNose6
#import Module1

import networkx as nx

def main():
    pass

if __name__ == '__main__':
    main()


Dir = 'C:\\WORK\\PROGRA~1\\DataTree\\PseudoDataGeneration\\Data\\simple\\'

listing = ["dicsimplelist_alpes.pseudosdostest",
"dicsimplelist_celine.pseudosdostest",
"dicsimplelist_chips.pseudosdostest",
"dicsimplelist_dog.pseudosdostest",
"dicsimplelist_fish.pseudosdostest",
"dicsimplelist_maman.pseudosdostest",
"dicsimplelist_papa.pseudosdostest",
"dicsimplelist_sexychoco.pseudosdostest",
"dicsimplerange_0.pseudosdostest",
"dicsimplerange_1.pseudosdostest",
"dicsimplerange_2.pseudosdostest",
"dicsimplerange_3.pseudosdostest",
"dicsimplerange_4.pseudosdostest",
"dicsimplerange_5.pseudosdostest",
"dicsimplerange_6.pseudosdostest",
"dicsimplerange_7.pseudosdostest",
"dicsimplerange_8.pseudosdostest",
"dicsimplerange_9.pseudosdostest",
"dicsimplelist_0_2.pseudosdostest",
"dicsimplelist_1_2.pseudosdostest",
"dicsimplelist_2_2.pseudosdostest",
"dicsimplelist_3_2.pseudosdostest",
"dicsimplelist_4_2.pseudosdostest",
"dicsimplelist_0_3.pseudosdostest",
"dicsimplelist_1_3.pseudosdostest",
"dicsimple2list_alpes.pseudosdostest",
"dicsimple2list_celine.pseudosdostest",
"dicsimple2list_chips.pseudosdostest",
"dicsimple2list_dog.pseudosdostest",
"dicsimple2list_fish.pseudosdostest",
"dicsimple2list_maman.pseudosdostest",
"dicsimple2list_papa.pseudosdostest",
"dicsimple2list_sexychoco.pseudosdostest",
"dicsimple2range_0.pseudosdostest",
"dicsimple2range_1.pseudosdostest",
"dicsimple2range_2.pseudosdostest",
"dicsimple2range_3.pseudosdostest",
"dicsimple2range_4.pseudosdostest",
"dicsimple2range_5.pseudosdostest",
"dicsimple2range_6.pseudosdostest",
"dicsimple2range_7.pseudosdostest",
"dicsimple2range_8.pseudosdostest",
"dicsimple2range_9.pseudosdostest",
"dicsimple2list_0_2.pseudosdostest",
"dicsimple2list_1_2.pseudosdostest",
"dicsimple2list_2_2.pseudosdostest",
"dicsimple2list_3_2.pseudosdostest",
"dicsimple2list_4_2.pseudosdostest"]
#myDataTree = myPseudoNose5.myPseudoNose( Dir, listing )
DirChaos = 'C:\\WORK\\PROGRA~1\\DataTree\\PseudoDataGeneration\\Data\\Chaos\\subdir\\'

listChaos=["dicchaos_11.pseudosdostest",
"dicchaos_13.pseudosdostest",
"dicchaos_15.pseudosdostest",
"dicchaos_21.pseudosdostest",
"dicchaos_211.pseudosdostest",
"dicchaos_33.pseudosdostest",
"dicchaos_35.pseudosdostest",
"dicchaos_44.pseudosdostest",
"dicchaos_45.pseudosdostest",
"dicchaos_5.pseudosdostest",
"dicchaos_55.pseudosdostest",
"dicchaos_6.pseudosdostest",
"dicchaos_66.pseudosdostest",
"dicchaos_69.pseudosdostest",
"dicchaos_8.pseudosdostest",
"dicchaos_88.pseudosdostest",
"dicchaos_90.pseudosdostest",
"dicchaos_91.pseudosdostest",
"dicchaos_92.pseudosdostest",
"dicchaos_93.pseudosdostest",
"dicchaos_94.pseudosdostest",
"dicchaos_95.pseudosdostest",
"dicchaos_96.pseudosdostest",
"dicchaos_97.pseudosdostest",
"dicchaos_98.pseudosdostest",
"dicchaos_99.pseudosdostest",
"dicchaos_xx1.pseudosdostest",
"dicchaos_xx2.pseudosdostest",
"dicchaos_xx3.pseudosdostest",
"dicchaos_xx4.pseudosdostest"]



listChaos=["dicchaos_11.pseudosdostest",
"dicchaos_13.pseudosdostest",
"dicchaos_15.pseudosdostest",
"dicchaos_6.pseudosdostest",
"dicchaos_66.pseudosdostest",
"dicchaos_69.pseudosdostest",
"dicchaos_8.pseudosdostest",
"dicchaos_88.pseudosdostest",
"dicchaos_xx1.pseudosdostest",
"dicchaos_xx2.pseudosdostest",
"dicchaos_xx3.pseudosdostest",
"dicchaos_xx4.pseudosdostest"]
'''
listChaos=["dicchaos_11.pseudosdostest",
"dicchaos_13.pseudosdostest",
"dicchaos_15.pseudosdostest",
"dicchaos_21.pseudosdostest",
"dicchaos_211.pseudosdostest",
"dicchaos_35.pseudosdostest",
"dicchaos_44.pseudosdostest",
"dicchaos_45.pseudosdostest",
"dicchaos_5.pseudosdostest",
"dicchaos_6.pseudosdostest",
"dicchaos_66.pseudosdostest",
"dicchaos_69.pseudosdostest",
"dicchaos_8.pseudosdostest",
"dicchaos_88.pseudosdostest",
"dicchaos_xx1.pseudosdostest",
"dicchaos_xx2.pseudosdostest",
"dicchaos_xx3.pseudosdostest",
"dicchaos_xx4.pseudosdostest"]
'''
'''listChaos=["dicchaos_5.pseudosdostest",
"dicchaos_15.pseudosdostest",
"dicchaos_6.pseudosdostest",
"dicchaos_21.pseudosdostest"]'''


'''"dicchaos_35.pseudosdostest",
"dicchaos_44.pseudosdostest",
"dicchaos_45.pseudosdostest",
"dicchaos_5.pseudosdostest",
"dicchaos_6.pseudosdostest"]'''
#"dicchaos_8.pseudosdostest"]
#,"dicchaos_69.pseudosdostest",
#"dicchaos_88.pseudosdostest"]'''

myDataTree = myPseudoNose6.myPseudoNose( DirChaos, listChaos )

