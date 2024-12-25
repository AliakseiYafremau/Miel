import { createSlice } from "@reduxjs/toolkit"

const ManagerSlice = createSlice({
    name: "manager",
    initialState: {
        manager: {candidates: []},
        candidate: {courses: []},
        candidates: {},
    },
    reducers: {
        setManager(state, action) {
            state.manager = action.payload
        },
        setCandidate(state, action) {
            state.candidate = action.payload
        },
        setCandidates(state, action) {
            state.candidates = action.payload
        },
    }
});

export const { setManager } = ManagerSlice.actions;
export const { setCandidate } = ManagerSlice.actions;
export const { setCandidates } = ManagerSlice.actions;

export default ManagerSlice.reducer;