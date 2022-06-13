import { useState } from 'react'

export default function CookieStandForm({ onCreate }) {

    const initialValues = {
        location: '',
        max: 0,
        min: 0,
        avg: 0,
    };

    const [values, setValues] = useState(initialValues);

    function submitHandler(event) {
        event.preventDefault();
        const reshapedData = reshapeData()
        onCreate(reshapedData);
        setValues(initialValues)
    }

    /*
    The api often requires a "reshaping" of the data to match.
    */
    function reshapeData() {
        return {
            location: values.location,
            minimum_customers_per_hour: values.min,
            maximum_customers_per_hour: values.max,
            average_cookies_per_sale: values.avg,
        }
    }

    function inputChangeHandler(event) {
        let { name, value, type } = event.target;

        if (type === "number") {
            value = parseFloat(value);
        }

        setValues({ ...values, [name]: value });
    }
    return (
        <form className="grid items-center justify-center grid-cols-3 gap-4 p-8 mx-auto my-4 text-center bg-green-200 border-2 border-green-400 rounded-lg text-md gap-x-8" onSubmit={submitHandler}>
            <div className="flex flex-col col-span-2 mb-4 ">
                <label className="mb-2 font-bold uppercase text-grey-darkest" htmlFor="location">Add Location</label>
                <input className="px-3 py-2 mx-8 border text-grey-darkest" type="text" name="location" id="location" value={values.location} onChange={inputChangeHandler} placeholder="Cookie Stand Location" />
            </div>

            <button className="p-4 uppercase bg-green-500 rounded text-green hover:bg-green-600" type="submit">Create Stand</button>


            <FormInputSection>
                <label className="mb-2 font-bold uppercase text-grey-darkest" htmlFor="min">Minimum Customers per Hour</label>
                <input className="px-3 py-2 mx-8 border text-grey-darkest" type="number" name="min" id="min" value={values.min} onChange={inputChangeHandler} />
            </FormInputSection>
            <FormInputSection>
                <label className="mb-2 font-bold uppercase text-grey-darkest" htmlFor="max">Maximum Customers per Hour</label>
                <input className="px-3 py-2 mx-8 border text-grey-darkest" type="number" name="max" id="max" value={values.max} onChange={inputChangeHandler} />
            </FormInputSection>
            <FormInputSection>
                <label className="mb-2 font-bold uppercase text-grey-darkest" htmlFor="avg">Average Cookies per Sale</label>
                <input className="px-3 py-2 mx-8 border text-grey-darkest" type="number" name="avg" id="avg" value={values.avg} onChange={inputChangeHandler} />
            </FormInputSection>
        </form>
    );
}

function FormInputSection({ children }) {
    return (
        <div className="flex flex-col justify-between">
            {children}
        </div>
    );
}
