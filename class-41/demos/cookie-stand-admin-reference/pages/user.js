import { useRouter } from 'next/router'
import { useAuth } from '../contexts/auth'
import { useEffect } from 'react'


export default function User() {
    const { user } = useAuth();
    const router = useRouter();

    useEffect(() => {
        if (!user) {
            router.push('/')
        }
    })


    return <h1>User {JSON.stringify(user)}</h1>
}