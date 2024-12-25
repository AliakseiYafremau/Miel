import React from "react"
import { useSelector, useDispatch } from "react-redux"

import "./DashBoardFilter.css"
import { setFilter, setFilterToggle } from "../../../store/slice/FilterSlice.js"
import { get } from "../../../export/api/api.js"
import { setCandidates } from "../../../store/slice/ManagerSlice.js"
import LoadingSVG from "../../SVG/Loading.jsx"


export default function DashBoardHeaderFilter() {
    const [load, setLoad] = React.useState(false)

    const filter = useSelector(state => state.Filter.filter)

    const dispatch = useDispatch()
    const set_filter = (obj) => dispatch(setFilter(obj))
    const set_candidates = (obj) => dispatch(setCandidates(obj))
    const set_filter_toggle = (obj) => dispatch(setFilterToggle(obj))

    const changeForm = {}
    Object.assign(changeForm, filter)

    function changeAge(e) {
        if (e.target.value < 0) {
            e.target.value = 0
        }
        if (e.target.value > 999) {
            e.target.value = 999
        }
        changeForm[e.target.dataset.field] = e.target.value
        set_filter(changeForm)
    }

    async function get_filter() {
        setLoad(true)
        const queryObj = {}
        Object.assign(queryObj, filter)
        Object.keys(queryObj).forEach(key => {
            if (!queryObj[key]) {
              delete queryObj[key];
            }
        })
        const query = new URLSearchParams(queryObj)
        await get(`manager/get_available_candidates?${query.toString()}`)
        .then(json => {
            if (!json.error && !json.detail) {
                set_candidates(json)
                setLoad(false)
                set_filter_toggle(false)
            }
        })
    }

    React.useEffect(() => {
        document.getElementsByTagName("main")[0].style.backgroundColor = "var(--color-gray-1)"
        return () => {document.getElementsByTagName("main")[0].style.backgroundColor = ""}
    }, [])

    return(
        <div className="dashboard-filter">
            <div className="dashboard-filter-age">
                <p className="bold">Возраст</p>
                <div>
                    <div>
                        <label htmlFor="min_age">от</label>
                        <input data-field="min_age" type="number" max="999" name="min_age" onChange={changeAge} defaultValue={filter.min_age}/>
                    </div>
                    <div>
                        <label htmlFor="max_age">до</label>
                        <input data-field="max_age" type="number" max="999" name="max_age" onChange={changeAge} defaultValue={filter.max_age}/>
                    </div>
                </div>
            </div>
            { load ? <button><div className="login-loading"><LoadingSVG fill="primary"/></div></button> : <button onClick={get_filter}>Применить фильтр</button>}
        </div>
    )
}