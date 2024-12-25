import React from "react"
import { createRoot } from "react-dom/client"
import { BrowserRouter } from "react-router-dom"
import { Provider } from "react-redux"
import { Route, Routes } from "react-router-dom"

import App from "./components/App.jsx"
import store from "./store/store.js"


createRoot(document.getElementById("root")).render(
<React.StrictMode>
        <BrowserRouter>
            <Provider store={store}>
                <Routes>
                    <Route path="/*" element={ <App /> } />
                </Routes>
            </Provider>
        </BrowserRouter>
</React.StrictMode>
)