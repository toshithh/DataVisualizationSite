function propertyGraph(name, elemID, prop, color="#ccccff"){
    var x = [];
    for (let i=0; i<window.data.length; i++){
        if (x.indexOf(window.data[i][name].toUpperCase())==-1){
            x.push(window.data[i][name].toUpperCase());
        }
    }
    x.sort();

    var y = [];
    for (let i=0; i<x.length; i++){
        y.push(0);
    }
    for (let i=0; i<window.data.length; i++){
        var t = window.data[i];
        let j = x.indexOf(t[name].toUpperCase());
        var v = t[prop];
        v = (v=="" || v=="None") ? 0: parseInt(v);
        y[j] += v;
        
    }

    if (document.getElementById("unknown").checked){
        if (x.indexOf("")!=-1){
            x[x.indexOf("")] = "UNKOWN "+name.toUpperCase();
        }
    }else{
        if (x.indexOf("")!=-1){
            let j = x[x.indexOf("")];
            x = x.slice(1, x.length)
            y = y.slice(1, y.length);
        }
    }

    var tck = true;
    if (window.innerWidth<501){
        tck = false;
    }
    
    new Chart(elemID, {
        type: "bar",
        data: {
            labels: x,
            datasets: [{
                backgroundColor: color,
                data: y
            }]
        },
        options: {
            responsive: true,
            legend: {display: false},
            scales: {
                xAxes: [{
                    ticks: {
                        display: tck,
                    }
                }]
            }
        },
    })
}



function CountGraph(name, elemID, color="rgba(0,0,255,0.2)"){
    var x = [];
    for (let i=0; i<window.data.length; i++){
        if (x.indexOf(String(window.data[i][name]).toUpperCase())==-1){
            x.push(String(window.data[i][name]).toUpperCase());
        }
    }
    x.sort();

    var y = [];
    for (let i=0; i<x.length; i++){
        y.push(0);
    }
    for (let i=0; i<window.data.length; i++){
        var t = window.data[i];
        let j = x.indexOf(String(t[name]).toUpperCase());
        y[j]+=1;
    }

    if (x.indexOf("")!=-1){
        let j = x[x.indexOf("")];
        x = x.slice(1, x.length)
        y = y.slice(1, y.length);
    }
    
    new Chart(elemID, {
        type: "line",
        data: {
            labels: x,
            datasets: [{
                backgroundColor: color,
                borderColor: "rgba(100,0,150,0.5)",
                //fill: false,
                data: y
            }]
        },
        options: {
            responsive: true,
            legend: {display: false},
        },
    })
}



function projectNum(name, elemID){
    var disp = true;
    var x = [];
    for (let i=0; i<window.data.length; i++){
        if (x.indexOf(window.data[i][name].toUpperCase())==-1){
            x.push(window.data[i][name].toUpperCase());
        }
    }
    x.sort();

    var y = [];
    for (let i=0; i<x.length; i++){
        y.push(0);
    }
    for (let i=0; i<window.data.length; i++){
        var t = window.data[i];
        let j = x.indexOf(t[name].toUpperCase());
        y[j]+=1;
    }

    var colors = [];
    for(let i=0;i<x.length;i++){
        colors.push('#'+Math.floor(Math.random()*16777215).toString(16));
    }

    if (document.getElementById("unknown").checked){
        if (x.indexOf("")!=-1){
            x[x.indexOf("")] = "UNKOWN "+name.toUpperCase();
        }
    }else{
        if (x.indexOf("")!=-1){
            let j = x[x.indexOf("")];
            x = x.slice(1, x.length)
            y = y.slice(1, y.length);
        }
    }

    if (x.length>10){
        disp = false;
    }
    console.log(x, y);
    if (window.innerHeight > window.innerWidth){
        var pos = 'bottom';
    }else{
        var pos = 'right';
    }
    new Chart(elemID, {
        type: "pie",
        data: {
          labels: x,
          datasets: [{
            backgroundColor: colors,
            data: y
          }]
        },
        options: {
            legend: {display: disp,
                position: pos,
            },
        }
      });
}