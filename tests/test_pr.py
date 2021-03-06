import sys
sys.path.append("../")
from ucsdpcb import PcbPlacer, PcbRouter, PcbDB

db = PcbDB.kicadPcbDataBase('../module/PCBBenchmarks/bm9/bm9.routed.kicad_pcb')
db.printNodes()
placer = PcbPlacer.GridBasedPlacer(db)
placer.set_num_iterations(1000)
placer.set_iterations_moves(25)
placer.set_two_sided(True)
placer.set_rtree(False)
placer.test_placer_flow()
db.printKiCad()
router = PcbRouter.GridBasedRouter(db)
router.set_grid_scale(20)
router.set_num_iterations(1)
router.set_enlarge_boundary(20)
router.set_layer_change_weight(1000)
router.route()
db.printKiCad()
