export default function CookieStandFooter({ reports }) {
    return (
        <footer className="p-4 mt-8 text-xl text-center text-gray-800 bg-green-500">
            {reports.length > 0 &&
                <p>{reports.length} Locations World Wide</p>
            }
        </footer>
    )
}
