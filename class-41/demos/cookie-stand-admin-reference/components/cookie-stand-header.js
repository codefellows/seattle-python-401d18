import Link from 'next/link'

export default function CookieStandHeader({ username, onLogout }) {
    return (
        <header className="flex items-center justify-around bg-green-400">
            <h1 className="py-4 text-4xl font-bold text-center text-gray-800">
                <Link href="/">
                    <a>Cookie Stand Admin</a>
                </Link>
            </h1>
            <div className="flex items-center gap-2 ">
                {username && <><Link href="/user" ><a className="px-3 py-1 text-gray-800 bg-green-100 rounded-lg">{username}</a></Link>
                    <Link href="/">
                        <a onClick={onLogout} className="px-3 py-1 text-gray-100 bg-green-600 rounded-lg">Sign Out</a>
                    </Link>
                    <nav>
                        <Link href="/overview"><a className="px-2 py-1 rounded bg-green-50">Overview</a></Link>
                    </nav>
                </>
                }
            </div>
        </header>
    )
}
