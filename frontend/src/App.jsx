import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import './App.css';

// API_BASE dinámico para Producción en servidor VPS
const API_BASE = window.location.hostname === 'localhost' 
  ? 'http://localhost:8000/api' 
  : `http://${window.location.hostname}:8000/api`;

function App() {
  const [modules, setModules] = useState([]);
  const [activeModule, setActiveModule] = useState(null);
  
  const [theoryContent, setTheoryContent] = useState('');
  const [scriptName, setScriptName] = useState('');
  const [scriptCode, setScriptCode] = useState('');
  
  const [activeTab, setActiveTab] = useState('THEORY'); // THEORY or CONSOLE
  
  const [consoleOutput, setConsoleOutput] = useState('> Selecciona un módulo y presiona "Ejecutar Script"');
  const [isRunning, setIsRunning] = useState(false);

  // Load modules on startup
  useEffect(() => {
    axios.get(`${API_BASE}/modules`)
      .then(res => {
        setModules(res.data.modules);
        if (res.data.modules.length > 0) {
          selectModule(res.data.modules[0]);
        }
      })
      .catch(err => console.error("Error cargando módulos", err));
  }, []);

  const selectModule = async (mod) => {
    setActiveModule(mod);
    setActiveTab('THEORY');
    setTheoryContent('Cargando teoría...');
    setScriptName('');
    setConsoleOutput('> Listo para ejecutar código...');
    
    try {
      const theoryRes = await axios.get(`${API_BASE}/modules/${mod.id}/theory`);
      setTheoryContent(theoryRes.data.content);
      
      const scriptRes = await axios.get(`${API_BASE}/modules/${mod.id}/script`);
      if (scriptRes.data.filename) {
        setScriptName(scriptRes.data.filename.replace(/\\/g, '/').split('/').pop());
        setScriptCode(scriptRes.data.source_code);
      } else {
        setScriptName('');
        setScriptCode('');
      }
    } catch (error) {
      console.error(error);
      setTheoryContent('# Error de conexión con el Backend Python.');
    }
  };

  const handleExecute = async () => {
    if (!activeModule) return;
    
    setIsRunning(true);
    setConsoleOutput(`> Ejecutando archivo ${scriptName}...\n> Por favor, espera. Si el LLM interactivo no está descargado, esto bajará Gigabytes localmente al ordenador y puede tardar varios minutos la primera vez...`);
    
    try {
      const res = await axios.post(`${API_BASE}/modules/${activeModule.id}/execute`);
      setConsoleOutput(`> Ejecución completada exitosamente.\n\n${res.data.output}`);
    } catch (error) {
      setConsoleOutput(`> [ERROR DE COMUNICACIÓN API]: El servidor FastAPI de Python no responde o está apagado. ${error.message}`);
    } finally {
      setIsRunning(false);
    }
  };

  return (
    <div className="app-container">
      
      {/* SIDEBAR */}
      <aside className="sidebar glass-panel">
        <h1>
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
            <path d="M2 17l10 5 10-5"></path>
            <path d="M2 12l10 5 10-5"></path>
          </svg>
          Hugging Face
        </h1>
        
        <div className="module-list">
          {modules.map(mod => (
            <button
              key={mod.id}
              onClick={() => selectModule(mod)}
              className={`module-button ${activeModule?.id === mod.id ? 'active' : ''}`}
            >
              <span>{mod.numero} - {mod.nombre}</span>
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <polyline points="9 18 15 12 9 6"></polyline>
              </svg>
            </button>
          ))}
        </div>
      </aside>

      {/* MAIN CONTENT */}
      <main className="main-content glass-panel">
        {activeModule ? (
          <>
            <div className="header-tabs">
              <button 
                className={`tab-btn ${activeTab === 'THEORY' ? 'active' : ''}`}
                onClick={() => setActiveTab('THEORY')}
              >
                Teoría Interactiva
              </button>
              <button 
                className={`tab-btn ${activeTab === 'CONSOLE' ? 'active' : ''}`}
                onClick={() => setActiveTab('CONSOLE')}
              >
                Ejecución de Código en la Nube
              </button>
            </div>

            <div className="content-scroll">
              {activeTab === 'THEORY' ? (
                <div className="markdown-body">
                  <ReactMarkdown>{theoryContent}</ReactMarkdown>
                </div>
              ) : (
                <div className="terminal-container">
                  {scriptName ? (
                    <>
                      <div className="source-code-viewer" style={{marginBottom: "1rem", maxHeight: "300px", overflowY: "auto", background: "rgba(0,0,0,0.5)", padding: "1rem", borderRadius: "8px", border: "1px solid var(--border-glow)"}}>
                        <h4 style={{marginTop: 0, marginBottom: "0.5rem", color: "var(--accent-cyan)"}}>Código Fuente ({scriptName})</h4>
                        <SyntaxHighlighter 
                          language="python" 
                          style={vscDarkPlus} 
                          showLineNumbers={true}
                          wrapLines={true}
                          customStyle={{margin: 0, borderRadius: '6px', fontSize: '0.85rem', fontFamily: "'Fira Code', monospace"}}
                        >
                          {scriptCode ? String(scriptCode).replace(/\r\n/g, '\n') : ''}
                        </SyntaxHighlighter>
                      </div>
                      <div className="run-header">
                        <span>$ python {scriptName}</span>
                        <button 
                          className="btn-run" 
                          onClick={handleExecute} 
                          disabled={isRunning}
                        >
                          {isRunning ? (
                            <><span className="loader"></span> Ejecutando IA...</>
                          ) : (
                            <>
                              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                <polygon points="5 3 19 12 5 21 5 3"></polygon>
                              </svg>
                              Correr Script
                            </>
                          )}
                        </button>
                      </div>
                      <div className="console-output">
                        {consoleOutput}
                      </div>
                    </>
                  ) : (
                    <div className="empty-state">
                      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                        <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path>
                        <line x1="12" y1="9" x2="12" y2="13"></line>
                        <line x1="12" y1="17" x2="12.01" y2="17"></line>
                      </svg>
                      <p>Este módulo es 100% teórico. No contiene ningún script ejecutable preparado por defecto.</p>
                      <button className="btn-run" onClick={() => setActiveTab('THEORY')} style={{fontSize: '0.9rem'}}>Volver a Teoría</button>
                    </div>
                  )}
                </div>
              )}
            </div>
          </>
        ) : (
          <div className="empty-state">
            <span className="loader"></span>
            <p>Conectando con el Servidor API Creado por Alejandro...</p>
          </div>
        )}
      </main>
      
    </div>
  );
}

export default App;
