"use strict";var KTFormsMultiselectsplitterDemos={init:function(){$("#kt_multiselectsplitter_example_1").multiselectsplitter(),$("#kt_multiselectsplitter_example_2").multiselectsplitter({selectSize:7,clearOnFirstChange:!0,groupCounter:!0}),$("#kt_multiselectsplitter_example_3").multiselectsplitter({groupCounter:!0,maximumSelected:2}),$("#kt_multiselectsplitter_example_4").multiselectsplitter({groupCounter:!0,maximumSelected:3,onlySameGroup:!0}),$("#kt_multiselectsplitter_example_5").multiselectsplitter({size:6,groupCounter:!0,maximumSelected:2,maximumAlert:function(t){alert("You choose "+(t+1)+" options. Are you crazy ?")},createFirstSelect:function(t,e){return'<option class="text-success">prefix - '+t+"</option>"},createSecondSelect:function(t,e){return'<option class="text-danger"> ??? </option>'}})}};KTUtil.onDOMContentLoaded((function(){KTFormsMultiselectsplitterDemos.init()}));
