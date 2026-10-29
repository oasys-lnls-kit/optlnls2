---
config:
  layout: elk
---
flowchart LR
 subgraph PHYSICS["Scientific Models"]
        SOURCES["Sources"]
        OPTICS["X-ray optics"]
        WAVEFRONT["Wavefront"]
        METROLOGY["Metrology"]
        oe["oe"]
        sources["sources"]
        wavefront["wavefront"]
        metrology["metrology"]
  end
 subgraph crystal["crystal"]
        c_init["__init__.py"]
        crystal.py["crystal.py"]
        models.py["models.py"]
  end
 subgraph oe["oe"]
        oe0["__init__.py"]
        crystal
        mirror
        fzp
  end
  subgraph wavefront["wavefront"]
    wave2D
  end
  subgraph metrology["metrology"]
    surface
  end
 subgraph sources["sources"]
        s_init["__init__.py"]
        undulator.py["undulator.py"]
        bending_magnet.py["bending_magnet.py"]
  end
 subgraph SUPPORT["Core Support"]
        DATA["Data Models"]
        models
        ANALYSIS["Analysis"]
        fitting
  end
 subgraph EXTERNAL["External Adapters"]
        io["io"]
        IO["File formats"]
        adapters["adapters"]
        INTEGRATIONS["SHADOW / SRW / xrt"]
  end
 subgraph VISUALIZATION["Visualization"]
        plot["plot"]
        PLOTTING["Plotting"]
  end
    OPTICS --> oe
    SOURCES --> sources
    WAVEFRONT --> wavefront
    METROLOGY --> metrology
    IO --> io
    INTEGRATIONS --> adapters
    PLOTTING --> plot
    DATA --> models
    ANALYSIS --> fitting
    crystal.py --> n1["Consumer entity implementation"]
    models.py --> n2["Dataclasses implementation"]
    oe0 --> n3["Lazy imports"]
    c_init --> n3

    n1@{ shape: comment}
    n2@{ shape: comment}
    n3@{ shape: comment}