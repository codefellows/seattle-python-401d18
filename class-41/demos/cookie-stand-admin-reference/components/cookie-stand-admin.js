import CookieStandForm from './cookie-stand-form'
import CookieStandTable from './cookie-stand-table'
import useResource from '../hooks/useResource'

export default function CookieStandAdmin({ onLogout }) {

    const { resources, createResource, deleteResource, error } = useResource();

    if (error) {
        onLogout();
        return null;
    }

    if (!resources) return <h2>Loading...</h2>

    return (
        <div>
            <CookieStandForm onCreate={createResource} />
            <CookieStandTable stands={resources} onDelete={deleteResource} />
        </div>
    )
}
