CSS = """
<style>
:root{
    --font-family: "JetBrains Mono", Consolas, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace;
    --base-font-size: 16px;
    --bg-color: #0a0015;
    --bg-gradient: linear-gradient(160deg, rgba(10,0,21,1) 0%, rgba(15,8,32,1) 40%, rgba(10,0,21,1) 100%);
    --panel-bg: #120825;
    --text-color: #f0e6ff;
    --muted-color: #d4c0ff;
    --accent-start: #c864ff;
    --accent-end: #9d4edd;
    --accent-shadow: rgba(200,100,255,0.75);
    --glass-border: rgba(180,100,255,0.5);
}

/* Light and Dark theme variables using user preference */
@media (prefers-color-scheme: dark){
    :root{
        --bg-color: #0a0015;
        --bg-gradient: linear-gradient(160deg, rgba(10,0,21,1) 0%, rgba(15,8,32,1) 40%, rgba(10,0,21,1) 100%);
        --panel-bg: #120825;
        --text-color: #f0e6ff;
        --muted-color: #d4c0ff;
        --accent-start: #c864ff;
        --accent-end: #9d4edd;
        --accent-shadow: rgba(200,100,255,0.75);
        color-scheme: dark;
    }
}

@media (prefers-color-scheme: light){
    :root{
        --bg-color: #fbf8ff;
        --bg-gradient: linear-gradient(160deg, #fbf8ff 0%, #f6f3ff 40%, #fbf8ff 100%);
        --panel-bg: #ffffff;
        --text-color: #0a0515;
        --muted-color: #5b4a6a;
        --accent-start: #7b4bff;
        --accent-end: #5a3bd6;
        --accent-shadow: rgba(90,60,180,0.12);
        --glass-border: rgba(90,60,180,0.12);
        color-scheme: light;
    }
}

/* Responsive font sizes by device width */
@media (max-width: 599px){
    :root{ --base-font-size: 14px; }
}
@media (min-width: 600px) and (max-width: 1199px){
    :root{ --base-font-size: 16px; }
}
@media (min-width: 1200px){
    :root{ --base-font-size: 18px; }
}

html, body, .gradio-container{ 
    font-family: var(--font-family);
    font-size: var(--base-font-size);
    background: var(--bg-gradient);
    color: var(--text-color);
    transition: background-color 220ms ease, color 220ms ease, box-shadow 220ms ease;
}

#title-wrap{ text-align:center; padding: 22px 0 10px 0; }

#title-wrap h1{
    font-size: 2.3rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--text-color);
    text-shadow: 0 0 14px rgba(200,100,255,0.12), 0 0 26px rgba(150,80,255,0.08);
}

#title-wrap p{ color: var(--muted-color); font-size: 0.95rem; }

.panel{
    max-width: 1200px; margin: 0 auto; background: var(--panel-bg);
    border-radius: 16px; border: 1px solid var(--glass-border); box-shadow: 0 18px 40px rgba(0,0,0,0.08);
    padding: 16px 18px 18px; transition: background 180ms ease, border-color 180ms ease;
}

label, .gradio-container .label{ color: var(--text-color) !important; font-weight:600; font-size:0.84rem; letter-spacing:0.04em; text-transform:uppercase; }

input, textarea, select{ background: rgba(0,0,0,0.03); color: var(--text-color); border-radius:10px; border:1px solid rgba(0,0,0,0.08); outline:none; }
input:focus, textarea:focus, select:focus{ box-shadow: 0 0 0 1px var(--accent-shadow); border-color: var(--accent-end); }

button, button.primary{ background: linear-gradient(90deg, var(--accent-start), var(--accent-end)); color: var(--panel-bg); font-weight:700; border-radius:999px; border:none; box-shadow: 0 0 18px var(--accent-shadow); text-transform:uppercase; letter-spacing:0.1em; font-size:0.88rem; padding:10px 18px; }
button:hover{ filter:brightness(1.06); }

.variant-output, .comparison-table{ max-width:1200px; margin:12px auto; border-radius:12px; padding:14px 16px; background: var(--panel-bg); border:1px solid var(--glass-border); box-shadow: 0 12px 30px rgba(0,0,0,0.06); overflow-x:auto; }

/* Size-specific utility classes (also set by JS fallback) */
.device-small #title-wrap h1{ font-size: 1.6rem; }
.device-medium #title-wrap h1{ font-size: 2.1rem; }
.device-large #title-wrap h1{ font-size: 2.6rem; }

/* High contrast preference */
@media (prefers-contrast: more){
    :root{ --accent-shadow: rgba(200,100,255,0.95); }
    .panel, .variant-output, .comparison-table{ box-shadow: none; border-width: 1.5px; }
}

</style>

<script>
// JS fallback for setting device size classes and a data-theme attribute
(function(){
    function applySizeClass(){
        var w = window.innerWidth || document.documentElement.clientWidth;
        document.documentElement.classList.remove('device-small','device-medium','device-large');
        if(w < 600) document.documentElement.classList.add('device-small');
        else if(w < 1200) document.documentElement.classList.add('device-medium');
        else document.documentElement.classList.add('device-large');
    }
    function applyThemeAttr(){
        try{
            var dark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
            document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
        }catch(e){}
    }
    applySizeClass(); applyThemeAttr();
    window.addEventListener('resize', applySizeClass);
    if(window.matchMedia){
        var mq = window.matchMedia('(prefers-color-scheme: dark)');
        if(mq.addEventListener) mq.addEventListener('change', applyThemeAttr);
        else if(mq.addListener) mq.addListener(applyThemeAttr);
    }
})();
</script>
"""