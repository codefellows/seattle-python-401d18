export default function EightBall({ answer }) {
    return (
        <div className="mx-auto bg-black rounded-full w-96 h-96">
            <div className="relative flex items-center justify-center w-64 h-64 bg-white rounded-full left-12 top-12">
                <p className="text-xl">{answer || 'Waiting...'}</p>
            </div>
        </div>
    );
}
