import { useAuth } from '../contexts/auth'
import useResource from '../hooks/useResource'
import CookieStandHeader from '../components/cookie-stand-header'
import CookieStandFooter from '../components/cookie-stand-footer'
import Head from 'next/head'

export default function Layout({ children }) {

    const { user, logout } = useAuth();
    const { resources } = useResource()


    return (
        <div>
            <Head>
                <title>Cookie Stand Admin</title>
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <CookieStandHeader username={user?.username} onLogout={logout} />
            <main className="w-5/6 mx-auto">{children}</main>
            <CookieStandFooter reports={resources || []} />
        </div>
    )
}
