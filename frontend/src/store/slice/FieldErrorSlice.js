import { createSlice } from "@reduxjs/toolkit"


const FieldErrorSlice = createSlice({
    name: "fieldError",
    initialState: {
        field: []
    },
    reducers: {
        setFieldError(state, action) {
            state.field = action.payload
        }
    }
});

export const { setFieldError } = FieldErrorSlice.actions;

export default FieldErrorSlice.reducer;