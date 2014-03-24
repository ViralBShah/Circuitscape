GUI_OPTIONS_RSRC = {'type':'CustomDialog',
    'name':'csOptions',
    'title':'Circuitscape options',
    'position':(371, 58),
    'size':(584, 684),
    'components': [

{'type':'StaticText', 
    'name':'rmvSrcGndTitle', 
    'position':(12, 180), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Advanced mode: when a source and ground are at the same node:', 
    },

{'type':'Choice', 
    'name':'rmvSrcGndChoice', 
    'position':(24, 204), 
    'size':(502, -1), 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 10}, 
    'items':[u'Remove source', u'Remove ground', u'Remove both source and ground', u'Keep both when possible but remove ground if source is tied directly to ground'], 
    'stringSelection':'Remove both source and ground', 
    },

{'type':'CheckBox', 
    'name':'lowMemBox', 
    'position':(12, 108), 
    'size':(581, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Pairwise mode: run in low-memory mode', 
    },

{'type':'CheckBox', 
    'name':'releaseMemBox', 
    'position':(12, 84), 
    'size':(581, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Preemptively release memory when possible', 
    },

{'type':'CheckBox', 
    'name':'cumMapBox', 
    'position':(12, 298), 
    'size':(303, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Write cumulative && max current maps only', 
    },

{'type':'CheckBox', 
    'name':'zeroCurrentsBox', 
    'position':(12, 322), 
    'size':(303, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Set focal node currents to zero', 
    },

{'type':'CheckBox', 
    'name':'maxMapBox', 
    'position':(12, 274), 
    'size':(246, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Write maximum of current maps', 
    },

{'type':'CheckBox', 
    'name':'compressGridsBox', 
    'position':(326, 274), 
    'size':(193, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Compress output grids', 
    },


{'type':'CheckBox', 
    'name':'logCurMapBox', 
    'position':(326, 298), 
    'size':(217, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Log-transform current maps', 
    },

{'type':'CheckBox', 
    'name':'unitSrcsBox', 
    'position':(12, 132), 
    'size':(437, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Advanced mode: use unit currents (i=1) for all current sources', 
    },

{'type':'CheckBox', 
    'name':'avgConductanceBox', 
    'position':(12, 60), 
    'size':(577, 21), 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Use average conductance instead of resistance for connections between cells', 
    },

{'type':'CheckBox', 
    'name':'directGndsBox', 
    'position':(12, 156), 
    'size':(593, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Advanced mode: use direct connections to ground (R=0) for all ground points', 
    },

{'type':'CheckBox', 
    'name':'connectFourNBox', 
    'position':(12, 36), 
    'size':(437, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Connect raster cells to FOUR neighbors instead of EIGHT', 
    },

{'type':'Button', 
    'name':'maskBrowse', 
    'position':(444, 408), 
    'size':(-1, 23), 
    'font':{'faceName': u'Lucida Grande', 'family': 'default', 'size': 11}, 
    'label':'Browse', 
    },

{'type':'TextField', 
    'name':'maskFile', 
    'position':(12, 408), 
    'size':(418, 21), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'text':'(Browse for a raster mask file)', 
    },

{'type':'CheckBox', 
    'name':'maskBox', 
    'position':(12, 384), 
    'size':(357, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Read raster mask file', 
    },

{'type':'StaticText', 
    'name':'calcOptionsTitle', 
    'position':(10, 12), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 13}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Calculation options', 
    },

{'type':'StaticText', 
    'name':'OPTIONS', 
    'position':(420, 6), 
    'font':{'style': 'bold', 'faceName': u'Arial', 'family': 'sansSerif', 'size': 20}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'OPTIONS', 
    },

{'type':'StaticText', 
    'name':'mappingOptions', 
    'position':(12, 248), 
    'font':{'style': 'bold', 'faceName': 'Lucida Grande', 'family': 'sansSerif', 'size': 13}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Mapping options', 
    },

{'type':'StaticText', 
    'name':'otherFilesTitle', 
    'position':(12, 360), 
    'font':{'style': 'bold', 'faceName': 'Lucida Grande', 'family': 'sansSerif', 'size': 13}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Optional input files', 
    },

{'type':'CheckBox', 
    'name':'polygonsBox', 
    'position':(12, 436), 
    'size':(377, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Load a raster short-circuit region map', 
    },

{'type':'TextField', 
    'name':'polygonFile', 
    'position':(12, 462), 
    'size':(418, 21), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'text':'(Browse for a short-circuit region file)', 
    },

{'type':'Button', 
    'name':'polygonBrowse', 
    'position':(444, 462), 
    'size':(-1, 23), 
    'font':{'faceName': u'Lucida Grande', 'family': 'default', 'size': 11}, 
    'label':'Browse', 
    },

{'type':'TextField', 
    'name':'varSrcFile', 
    'position':(12, 516), 
    'size':(418, 21), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'text':'(Browse for a source strength file)', 
    },

{'type':'Button', 
    'name':'varSrcBrowse', 
    'position':(444, 516), 
    'size':(-1, 23), 
    'font':{'faceName': u'Lucida Grande', 'family': 'default', 'size': 11}, 
    'label':'Browse', 
    },

{'type':'CheckBox', 
    'name':'varSrcBox', 
    'position':(12, 492), 
    'size':(437, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'One-to-all and All-to-one modes: read source strength file', 
    },

{'type':'CheckBox', 
    'name':'includePairsBox', 
    'position':(12, 546), 
    'size':(449, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Pairwise mode: read file with focal node pairs to include/exclude', 
    },

{'type':'Button', 
    'name':'includePairsBrowse', 
    'position':(444, 570), 
    'size':(-1, 23), 
    'font':{'faceName': u'Lucida Grande', 'family': 'default', 'size': 11}, 
    'label':'Browse', 
    },

{'type':'TextField', 
    'name':'includePairsFile', 
    'position':(12, 570), 
    'size':(418, 21), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'text':'(Browse for a file with pairs to include or exclude)', 
    },

{'type':'Button', 
    'id':5100, 
    'name':'btnOK', 
    'position':(330, 612), 
    'size':(81, 29), 
    'default':1, 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 10}, 
    'label':'OK', 
    },

{'type':'Button', 
    'id':5101, 
    'name':'btnCancel', 
    'position':(426, 612), 
    'size':(87, 29), 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 10}, 
    'label':'Cancel', 
    },

] # end components
} # end CustomDialog