import React from "react"
import { useDispatch, useSelector } from "react-redux"

import "./Candidate.css"
import StickyNoteSVG from "../../SVG/StickyNote.jsx"
import LoadingSVG from "../../SVG/Loading.jsx"
import DownloadSVG from "../../SVG/Download.jsx"
import { get, postManager } from "../../../export/api/api.js"
import { setCandidate, setManager } from "../../../store/slice/ManagerSlice.js"


export default function Candidate() {
    const urlParams = new URLSearchParams(window.location.search)
    const id = urlParams.get('id')

    const [note, setNote] = React.useState(true)
    const [default_note, setDefaultNote] = React.useState("")
    const [invited, setInvited] = React.useState(false)
    const [load, setLoad] = React.useState(false)

    const candidate = useSelector(state => state.Manager.candidate)
    const manager = useSelector(state => state.Manager.manager)

    const dispatch = useDispatch()
    const set_candidate = (obj) => dispatch(setCandidate(obj))
    const set_manager = (obj) => dispatch(setManager(obj))

    let text = ""

    function focus() {
        setNote(false)
    }

    function blur() {
        setNote(true)
    }

    async function get_candidate() {
        await get(`manager/get_candidate_by_id?candidate_id=${id}`)
        .then(json => {
            set_candidate(json)
        })
    }

    function findInvited() {
        if (manager.candidates) {
            manager.candidates.map(can => {            
                if (can.candidate_id == candidate.id) {
                    setInvited(true)
                }
            })
        }
    }

    async function invite() {     
        setLoad(true)
        await postManager("invitation/invite_candidate/", {"id": candidate.id})
        .then(json => {
            if (!json.error && !json.detail) {
                getManager()
                setLoad(false)
                setInvited(true)
            }
        })
    }

    async function getManager() {
        await get("manager/")
        .then(json => {
            if (!json.error && !json.detail) {
                set_manager(json)
            }
        })
    }

    React.useEffect(() => {
        manager.candidates.map((can) => {
            if (can.candidate_id == candidate.id) {
                setDefaultNote(can.note)                
            }
        })
        
        findInvited()
    }, [candidate])

    React.useEffect(() => {
        get_candidate()
        if (!note) {
            document.getElementById("q").focus()
            document.getElementById("q").setSelectionRange(text.length, text.length)
        }
    }, [note])

    return( 
        <div className="candidate-card">
            { !invited ? <>{load ? <button><div className="login-loading"><LoadingSVG fill="primary"/></div></button> : <button onClick={invite}>Пригласить</button> } </> : <button className="candidate-card-invited">Приглашён</button>}
            <div className="candidate-card-note" onClick={focus}>
                <textarea id="q" className="w2" name="note" rows="2" maxLength="80" onFocus={focus} onBlur={blur} defaultValue={default_note}></textarea>
                {note ? <><StickyNoteSVG fill="gray"/>
                <label htmlFor="note">Заметка</label></> : ""}
            </div> 
            <div className="candidate-card-study">
                <div>
                    <p><span className="bold">ХОД ОБУЧЕНИЯ</span></p>
                    <p>Дата регистрации: {new Date(candidate.created_at).toLocaleDateString('en-GB').replace(/\//g, ".")}</p>
                </div>
                <table className="candidate-card-study-table">
                    <thead></thead>
                    <tbody>
                        { candidate.courses ? candidate.courses.map(curse => <tr key={curse.id}><td>{curse.course.name}</td><td>Пройдено</td></tr>) : <tr><td></td><td></td></tr>}
                    </tbody>
                </table>
            </div>
            <div>
                <p><span className="bold">НАВЫКИ</span></p>
                <div>
                    <DownloadSVG fill="black"/>
                    <p>резюме</p>
                </div>
            </div>
            <div>
                { candidate.skills ? candidate.skills.map((skill, id) => <div key={id}>{skill.skill.name}</div>) : ""}
            </div>
            <table className="candidate-card-table">
                <thead></thead>
                <tbody>
                    <tr><td>Приглашений</td><td>0</td></tr>
                    <tr><td>Объекты</td><td>{candidate.objects}</td></tr>
                    <tr><td>Клиенты</td><td>{candidate.clients}</td></tr>
                </tbody>
            </table>
        </div>
    )
}